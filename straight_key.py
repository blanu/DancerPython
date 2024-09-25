from enum import Enum

class LastSentType(Enum):
    LETTER = 0
    SPACE = 1

class StraightKey:
    characterSpeed: int

    def __init__(self):
        self.last_sent = LastSentType.SPACE

        # ARRL Morse Transmission Timing Standard
        # https:#www.arrl.org/files/file/Technology/x9004008.pdf

        self.characterSpeed = 18 # words per minute
        self.unitTime = 0 # milliseconds
        self.dotTime = 0 # milliseconds
        self.dashTime = 0 # milliseconds
        self.signalSpaceTime = 0 # milliseconds
        self.letterSpaceTime = 0 # milliseconds
        self.wordSpaceTime = 0 # milliseconds

        self.calculateTimings(self.characterSpeed)

    def calculateTimings(self, c):
          if c >= 18:
            # Standard Timing - At speeds at or about 18 wpm, standard timing will be used.
            u = 1.2 / float(c) # period of one unit, in seconds
            self.dotTime = int(u * 1000) # integer approximation of time for a dot signal in millisecond
            self.dashTime = int((u * 3) * 1000) # integer approximation of time for a dash signal in milliseconds
            self.signalSpaceTime = int(u * 1000) # integer approximation of inter-element spacing in millisecond
            self.letterSpaceTime = int((u * 3) * 1000) # integer approximation of space between characters in milliseconds
            self.wordSpaceTime = int((u * 7) * 1000) # integer approximation of space between words in milliseconds
          elif c == 12:
            # 12 wpm is a special case because this is the standard speed for Coherent CW (CCW). When 12 wpm is selected, the standardized CCW timing is used to ensure compatibility with CCW receivers.
            # Coherent CW: Amateur Radio's New State of the Art? by Raymond C. Petit, W7GHM, September 1975 - https:#www.arrl.org/files/file/Technology/tis/info/pdf/7509026.pdf
            # NOTES on COHERENT CW (CCW) - https:#www.qsl.net/dj7hs/ccwnotes.htm
            # COHERENT CW: Some Theory - https:#www.qsl.net/dj7hs/ccwtheo.htm
            self.dotTime = 100 # 100 milliseconds
            self.dashTime = 300 # 300 milliseconds
            self.signalSpaceTime = 100 # 100 milliseconds
            self.letterSpaceTime = 300 # 300 milliseconds
            self.wordSpaceTime = 700 # 700 milliseconds
          else:
            # Farnsworth Timing - At speeds below 18 wpm, characters are sent using 18-wpm timing, but with extra delay added between characters and words to produce an overall lower speed.
            s = float(c) # the overall transmission speed
            c = 18 # the character speed
            u = 1.2 / float(c) # period of one unit, in seconds
            self.dotTime = int(u * 1000) # integer approximation of time for a dot signal in millisecond
            self.dashTime = int((u * 3) * 1000) # integer approximation of time for a dash signal in milliseconds
            self.signalSpaceTime = int(u * 1000) # integer approximation of inter-element spacing in millisecond
            ta = ((60 * c) - (37.2 * s)) / (s * c) # total delay to add to the characters of a standard 50-unit word, in seconds
            tc = (3.0 * ta) / 19.0 # delay between characters
            tw = (7.0 * ta) / 19.0 # delay between words
            self.letterSpaceTime = int(tc * 1000) # integer approximation of space between characters in milliseconds, with added Farnsworth delay
            self.wordSpaceTime = int(tw * 1000) # integer approximation of space between words in milliseconds, with added Farnsworth delay

    def enterDash(self):
        pass

    def enterDot(self):
        pass

    def increaseCharacterSpeed(self):
        self.changeCharacterSpeed(self.characterSpeed + 1)

    def decreaseCharacterSpeed(self):
        self.changeCharacterSpeed(self.characterSpeed - 1)

    def changeCharacterSpeed(self, newCharacterSpeed):
        if newCharacterSpeed < 1:
            return

        if newCharacterSpeed > 160:
            return

        self.characterSpeed = newCharacterSpeed

        if newCharacterSpeed == 12:
            print("%d (CCW)" % self.characterSpeed)
        else:
            print("%d" % self.characterSpeed)

        self.calculateTimings(self.characterSpeed)

    def getCharacterSpeed(self):
        return self.characterSpeed

    def backspace(self):
        pass

    def sendSpace(self):
        pass

