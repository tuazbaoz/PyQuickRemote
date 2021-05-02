import re
import _thread
import Ultities
from xTimer import TimeMeasure
from xTimer import TimeObject
from xTimer import TimeFlags

class TimeFormatTemplates:
    Simple = 'Timer: Hour:@hour - Minute:@minute - Second:@second'
    LargeScreen = """
    Timer
    ==========================
        Year    : @year         
        Month   : @month         
        Day     : @day
        Hour    : @hour
        Minute  : @minute
        Second  : @second            
    =========================="""

class Timer():
    def __init__(self):
        self.__TimeObject = TimeObject()

    @property
    def Counter(): pass
    @Counter.setter
    def Counter(self, value):
        self.__TimeObject.Second = value
    @Counter.getter
    def Counter(self):
        return self.__TimeObject.Second

    @property
    def TimeFormat(): pass
    @TimeFormat.setter
    def TimeFormat(self, value):
        self.__TimeObject.FormatMask = value
    @TimeFormat.getter
    def TimeFormat(self):
        return self.__TimeObject.FormatMask
        
    @property
    def TimeText(): pass
    @TimeText.getter
    def TimeText(self):
        return self.__TimeObject.getFormattedString()
    
    @staticmethod
    def createInstanceFrom(TimeFormatMask: str):
        NewTimer = Timer()
        NewTimer.TimeFormat = TimeFormatMask
        return NewTimer

    #behaviors
    def __tick(self, TickDistance = 0):
        Ultities.Wait(TickDistance)
        self.Counter = self.Counter + TickDistance
        # self.showTime()

    def __turnOn(self, TickDistance = 1, SecondTimer = 86400, IsKeepRunning = False):
        if IsKeepRunning:
            while True: self.__tick(TickDistance= TickDistance)
        else:
            while self.Counter <= SecondTimer:
                self.__tick(TickDistance)

    def showTime(self):
        print(f'{self.TimeText}')   


    #Timer commands
    def startBackground(self, TickDistance = 1):
        """start timer has delay as the TickDistance.
        """
        Lock = _thread.allocate_lock()
        Ultities.startNewThreadFrom(Lock  , self.__turnOn, TickDistance, 0, True)