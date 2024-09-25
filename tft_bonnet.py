import board
from digitalio import DigitalInOut, Direction

from interface import Interface

class TFTBonnet:
    def __init__(self, interface):
        self.interface = interface

        self.state =    [False, False, False, False, False, False, False]
        self.oldState = [False, False, False, False, False, False, False]

        self.up = 0
        self.down = 1
        self.left = 2
        self.right = 3
        self.a = 4
        self.b = 5
        self.c = 6

        self.button_A = DigitalInOut(board.D5)
        self.button_A.direction = Direction.INPUT

        self.button_B = DigitalInOut(board.D6)
        self.button_B.direction = Direction.INPUT

        self.button_L = DigitalInOut(board.D27)
        self.button_L.direction = Direction.INPUT

        self.button_R = DigitalInOut(board.D23)
        self.button_R.direction = Direction.INPUT

        self.button_U = DigitalInOut(board.D17)
        self.button_U.direction = Direction.INPUT

        self.button_D = DigitalInOut(board.D22)
        self.button_D.direction = Direction.INPUT

        self.button_C = DigitalInOut(board.D4)
        self.button_C.direction = Direction.INPUT

        # Turn on the Backlight
        self.backlight = DigitalInOut(board.D26)
        self.backlight.switch_to_output()
        self. backlight.value = True

    def process(self):
        found = self.read()
        if found == self.up:
            self.interface.processUp()
        elif found == self.down:
            self.interface.processDown()
        elif found == self.left:
            self.interface.processLeft()
        elif found == self.right:
            self.interface.processRight()
        elif found == self.a:
            self.interface.processA()
        elif found == self.b:
            self.interface.processB()
        elif found == self.c:
            self.interface.processC()

    def read(self):
        self.state[self.up] = not self.button_U.value
        self.state[self.down] = not self.button_D.value
        self.state[self.left] = not self.button_L.value
        self.state[self.right] = not self.button_R.value
        self.state[self.a] = not self.button_A.value
        self.state[self.b] = not self.button_B.value
        self.state[self.c] = not self.button_C.value

        found = []
        for position in [self.up, self.down, self.left, self.right, self.a, self.b, self.c]:
            if self.state[position] and not self.oldState[position]:
                found.append(position)
            self.oldState[position] = self.state[position]

        if len(found) == 1:
            return found[0]
        else:
            return []
