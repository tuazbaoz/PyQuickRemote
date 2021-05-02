import time
import datetime
import sys
import traceback
from Bot import Bot

class LoggingSymbolTemp:
    LeftBlock  = '=====['
    RightBlock = ']====='

class Logging:
    LOG_FILE_NAME = r'.logs.log'

    @staticmethod
    def Log(Except: Exception, isExit = False):
        """Log the exception to log file, set isExit is true if
        you need to force the current app to exit.
        """
        Logging.writeToLogFile(Except)
        Logging.forceToExit(isExit)

    @staticmethod 
    def forceToExit(isExit):
        if(isExit == True): 
            Bot.showMessage('Force to kill app/background', Bot.ERROR)
            sys.exit()

    @staticmethod
    def writeToLogFile(Except):
        with open(Logging.LOG_FILE_NAME, mode = 'a') as logFile:
            Traceback = traceback.TracebackException.from_exception(Except).format()
            now = datetime.datetime.now()
            logFile.write(LoggingSymbolTemp.LeftBlock)
            logFile.writelines(str(now))
            logFile.write(LoggingSymbolTemp.RightBlock)
            logFile.writelines(Traceback)
