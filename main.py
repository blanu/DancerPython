from digitalio import DigitalInOut, Direction
import keyboard
import time

from tft_bonnet import TFTBonnet
from interface import Interface

class Dancer:
    def __init__(self):
        self.interface = Interface()
        self.bonnet = TFTBonnet(interface)

        while True:
            self.bonnet.process()

            time.sleep(0.01)

if __name__ == '__main__':
    dancer = Dancer()

keyboard.write('test')