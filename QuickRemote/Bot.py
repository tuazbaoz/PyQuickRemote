
#When the app has err/warning, message out by this class's staticMethods
class Bot:
    MAILER = 'BOT_MAILER'
    LOGGER = 'BOT_LOGGER'
    ERROR  = 'BOT_ERROR'
    SUCCESS = 'BOT_SUCCESSOR'
    REPRESENTER = 'BOT_REPRESENTER'

    @staticmethod
    def showMessage(Message: str, Representer = 'BOT'):
        """Print the given Message to terminal with representer is 
        the Representer.
        """
        print(f'{Representer}: {Message}')

    @staticmethod
    def showRawMessage(Message: str):
        """Print raw message to terminal.
        """
        print(f'{Message}')
