from virtual_keyboard import VirtualKeyboard

class Signals:
    def __init__(self):
        self.output = VirtualKeyboard()

        self.MAX_SIGNALS_LENGTH = 255
        self.signals = ''
        self.dictionary = {
            '.': 'e',
            '-': 't',
            '..': 'i',
            '.-': 'a',
            '-.': 'n',
            '--': 'm',
            '...': 's',
            '..-': 'u',
            '.-.': 'r',
            '.--': 'w',
            '-..': 'd',
            '_._': 'k',
            '--.': '',
            '---': 'o',
            '....': 'h',
            '...-': 'v',
            '..-.': 'f',
#           '..--'
            '.-..': 'l',
#           '.-.-'
            '.--.': 'p',
            '.---': 'j',
            '-...': 'b',
            '-..-': 'x',
            '-.-.': 'c',
            '-.--': 'y',
            '--..': 'z',
            '--.-': 'q',
#           '---.'
#           '----'
            '.....': '5',
            '....-': '4',
            '...--': '3',
            '..---': '2',
            '.----': '1',
            '-----': '0',
            '-....': '6',
            '--...': '7',
            '---..': '8',
            '----.': '9',
            '-...-': '=',
            '..--..': '?',
            '--..--': ',',
            '.-.-.-': '.',
            '.-...': '&'
        }

    def characterStarted(self):
        return len(self.signals) > 0

    def enterDot(self):
        if len(self.signals) < self.MAX_SIGNALS_LENGTH:
            self.signals += '.'

    def enterDash(self):
        if len(self.signals) < self.MAX_SIGNALS_LENGTH:
            self.signals += '-'

    def endCharacter(self):
        self.interpretCharacter(self.signals)
        self.signals = ''

        self.displayMessage()

    def enterSpace(self):
        self.signals += ' '

    def backspace(self):
        if len(self.signals) > 0:
            self.signals = self.signals[:-1]

    def clear(self):
        self.signals = ''

    def sendMessage(self):
        pass

    def displayMessage(self):
        pass

    def interpretCharacter(self, character):
        if character in self.dictionary:
            letter = self.dictionary[character]
            self.output.send(letter)