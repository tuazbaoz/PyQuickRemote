from Logging import Logging
import Ultities

class RisingException():
    def __init__(self, Message: str, Identifier: Ultities.EMPTY_STRING):
        """Message: Exception error message.\n
        Identifier: Exception notaion codeID. (non-required)
        """
        self.__Message = Message
        self.__Identifier = Identifier
    
    def __str__(self):
        return self.ExceptionString

    @property
    def ExceptionString(): pass
    @ExceptionString.getter
    def ExceptionString(self) -> str:
        return f"{self.__Identifier}: {self.__Message}"

    #rise and log exception with the give Message and Identifier
    @staticmethod
    def rise(Message: str, Identifier: Ultities.EMPTY_STRING):
        """Message: Exception error message.\n
        Identifier: Exception notation codeID. (non-required)
        """
        Except = Exception(RisingException(Message, Identifier))
        raise(Except)