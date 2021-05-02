import Ultities
import re
from RisingException import RisingException

class TimeFlags:
    YEAR = 'year'
    MONTH = 'month'
    DAY = 'day'
    HOUR = 'hour'
    MINUTE = 'minute'
    SECOND = 'second'

class TimeObject():
    def __init__(self, 
                    Year = 0, Month = 0, 
                    Day = 0, Hour = 0,
                    Minute = 0, second = 0):
        self.__year = Year
        self.__month = Month
        self.__day = Day
        self.__hour = Hour
        self.__minute = Minute
        self.__second = second
        self.__FormatMask = '@hourH:@minuteM:@secondS'

    def __str__(self):
        return self.__format(self.__FormatMask)

    #FORMAT-MASK
    @property
    def FormatMask():pass
    @FormatMask.setter
    def FormatMask(self, value: str):
        if TimeObject.isValidTimeFormat(value): self.__FormatMask= value
        else: RisingException.rise('Invalid timer format', 'to1')
    @FormatMask.getter
    def FormatMask(self):
        return self.__FormatMask

    #YEAR
    @property
    def Year():pass
    @Year.setter
    def Year(self, value):
        if self.IsValidInputTimeMeasure(value, 'year'): self.__year = value
        else: RisingException.rise("can't set time value",'to2')
    @Year.getter
    def Year(self): return self.__year

    #MONTH
    @property
    def Month():pass
    @Month.setter
    def Month(self, value):
        if self.IsValidInputTimeMeasure(value, 'month'): self.__month = value
        else: RisingException.rise("can't set time value",'to2')
    @Month.getter
    def Month(self): return self.__month

    #DAY
    @property
    def Day():pass
    @Day.setter
    def Day(self, value):
        if self.IsValidInputTimeMeasure(value, 'day'): self.__day = value
        else: RisingException.rise("can't set time value",'to2')
    @Day.getter
    def Day(self): return self.__day

    #HOUR
    @property
    def Hour():pass
    @Hour.setter
    def Hour(self, value):
        if self.IsValidInputTimeMeasure(value, 'hour'): self.__hour = value
        else: RisingException.rise("can't set time value",'to2')
    @Hour.getter
    def hour(self): return self.__hour

    #MINUTE
    @property
    def Minute():pass
    @Minute.setter
    def Minute(self, value):
        if self.IsValidInputTimeMeasure(value, 'minute'): self.__minute = value
        else: RisingException.rise("can't set time value",'to2')
    @Minute.getter
    def Minute(self): return self.__minute

    #SECOND
    @property
    def Second():pass
    @Second.setter
    def Second(self, value):
        if self.IsValidInputTimeMeasure(value, 'second'): self.__second = value
        else: RisingException.rise("can't set time value",'to2')
    @Second.getter
    def Second(self): return self.__second

    #total SECONDs
    @property
    def TotalSecond():pass
    @TotalSecond.getter
    def TotalSecond(self):
        Dict = self.getDictionary()
        return sum(Dict[TimeType]*TimeMeasure.SecondPerTimeTypeDictionary[TimeType] for TimeType in Dict)

    #BEHAVIOR
    def getDictionary(self):
        return TimeMeasure.createDictionaryTime(self.__year,self.__month,self.__day,
                                             self.__hour, self.__minute, self.__second)
    
    def IsValidInputTimeMeasure(self, value, Name):
        return value >= 0 or self.TotalSecond - self.__year*TimeMeasure.SecondPerTimeTypeDictionary[Name]

    def getFormattedString(self):
        DictionaryTime = self.getDictionary()
        BeautyDictionaryTime = TimeMeasure.getBeautyDictionaryTimeFrom(DictionaryTime, 
                                *TimeObject.getTimeTagNamesFrom(self.__FormatMask))
        BeautyTimeObject = TimeObject.CreateTimeObjectFrom(BeautyDictionaryTime)
        BeautyTimeObject.FormatMask = self.FormatMask
        return str(BeautyTimeObject)

    def __replaceTimeText(self, TimeType, Text, replace_text):
        return re.sub(f'@{TimeType}', replace_text, Text)

    def __format(self, Mask: str):
        # @year @month @day @hour @minute @second
        # ex: @dayd-@hourh -> 25d-14h
        DictionaryTime = self.getDictionary()
        SecondPerTimeTypeDictionary = TimeMeasure.SecondPerTimeTypeDictionary
        for TimeType in SecondPerTimeTypeDictionary:
            Mask = self.__replaceTimeText(TimeType, Mask, str(DictionaryTime[TimeType]) )
        return Mask
    
    @staticmethod
    def CreateTimeObjectFrom(DictionaryTime: dict):
        return TimeObject(DictionaryTime['year'], DictionaryTime['month'], DictionaryTime['day'],
                            DictionaryTime['hour'], DictionaryTime['minute'], DictionaryTime['second'])

    @staticmethod
    def isValidTimeFormat(Text: str):
        TimeTags = TimeMeasure.getTimeTagNames()
        TimeTagPattern = '|'.join(TimeTags)
        SearchResult = re.search(f'@({TimeTagPattern})', Text, re.IGNORECASE)
        return Ultities.isNotNone(SearchResult)

    @staticmethod
    def getTimeTagNamesFrom(Text: str):
        TimeTags = TimeMeasure.getTimeTagNames()
        TimeTagPattern = '|'.join(TimeTags)
        SearchResult = re.findall(f'@({TimeTagPattern})', Text, re.IGNORECASE)
        return SearchResult


class TimeMeasure:
    SecondPerTimeTypeDictionary = {'year':31556926, 'month':2629743.83,
                                    'day':86400, 'hour':3600,
                                    'minute':60,'second':1}
    @staticmethod
    def getTotalSecondFrom(DictionaryTime: dict):
        return sum(DictionaryTime[TimeType]*TimeMeasure.SecondPerTimeTypeDictionary[TimeType] for TimeType in DictionaryTime)

    @staticmethod
    def getTimeTagNames():
        return [f'{TagName}' for TagName in TimeMeasure.SecondPerTimeTypeDictionary]

    @staticmethod
    def createDictionaryTime(Year= 0, Month=0, Day=0, Hour=0,Minute=0, Second=0):
        return {'year':Year, 'month':Month,
                'day':Day, 'hour':Hour,
                'minute':Minute,'second':Second}
    
    @staticmethod
    def getBeautyTimeObjectFrom(TimeObj: TimeObject, *TimeTypes: str):
        TempDictionaryTime = TimeObj.getDictionary()
        BeautyDictionaryTime = TimeMeasure.getBeautyDictionaryTimeFrom(TempDictionaryTime)
        return TimeObject.CreateTimeObjectFrom(BeautyDictionaryTime)

    @staticmethod
    def getBeautyDictionaryTimeFrom(DictionaryTime: dict, *TimeTypes: str):
        TotalSecondRemain = TimeMeasure.getTotalSecondFrom(DictionaryTime)
        TempDictionaryTime = TimeMeasure.createDictionaryTime(Second= TotalSecondRemain)
        SecondPerTimeTypeDictionary = TimeMeasure.SecondPerTimeTypeDictionary
        for TimeType in SecondPerTimeTypeDictionary:
            if TimeType in TimeTypes and TimeType != 'second':
                SecondNumber = SecondPerTimeTypeDictionary[TimeType]
                TempDictionaryTime[TimeType] = Ultities.roundLeft(TempDictionaryTime['second']/SecondNumber)
                TempDictionaryTime['second'] -= TempDictionaryTime[TimeType]*SecondPerTimeTypeDictionary[TimeType]
        TempDictionaryTime['second'] = round(TempDictionaryTime['second'])
        return TempDictionaryTime