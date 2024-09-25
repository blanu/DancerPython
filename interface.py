from enum import Enum
from signals import Signals
from straight_key import StraightKey

class StickMode(Enum):
    HORIZONTAL = 0
    VERTICAL = 1

class Interface:
    def __init__(self):
        self.stickDirection = StickMode.HORIZONTAL
        self.signals = Signals()
        self.straight_key = StraightKey()

    def processUp(self):
        if self.stickDirection == StickMode.VERTICAL:
            self.straight_key.increaseCharacterSpeed()
        else:
            self.signals.enterDot()

    def processDown(self):
        if self.stickDirection == StickMode.VERTICAL:
            self.straight_key.decreaseCharacterSpeed()
        else:
            self.signals.enterDash()

    def processLeft(self):
        if self.stickDirection == StickMode.HORIZONTAL:
            self.signals.enterDot()
        else:
            self.straight_key.increaseCharacterSpeed()

    def processRight(self):
        if self.stickDirection == StickMode.HORIZONTAL:
            self.signals.enterDash()
        else:
            self.straight_key.decreaseCharacterSpeed()

    def processA(self):
        if self.signals.characterStarted():
            self.signals.endCharacter()
        else:
            self.signals.enterSpace()

    def processB(self):
        self.signals.backspace()

    def processC(self):
        self.signals.clear()

    def processD(self):
        if self.stickDirection == StickMode.HORIZONTAL:
            self.stickDirection = StickMode.VERTICAL
        else:
            self.stickDirection = StickMode.HORIZONTAL

