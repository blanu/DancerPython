import keyboard

class VirtualKeyboard:
    def __init__(self):
        self.shiftOn = False

    def shift(self):
        self.shiftOn = True

    def send(self, letter):
        if self.shiftOn:
            keyboard.write(letter.to_uppercase())
        else:
            keyboard.write(letter)