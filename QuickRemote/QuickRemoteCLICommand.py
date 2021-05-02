import re
import Ultities
import sys, _thread
import os
import gc
from Logging import Logging
from Gmail import Gmail
from Timer import Timer
from Timer import TimeFormatTemplates
from CodeServer import CodeServer
from NgrokServer import NgrokServer
from Settings import RemoteSetting
from RisingException import RisingException
from Bot import Bot

class QuickRemoteCLICommand:
    __WARNING="""
Must complete your settings first!
Change [.settings.json] file follow the
template:
        "BotGmail": "example@gmail.com",
        "BotGmailPassword": "example@123456",
        "SuPassword": "enterYourSudoPassword",
        "RemoteEmail": "yourRemoteEmail@gmail.com",
        "NgrokLaunchPath": "/ngrokDirectory/ngrok",
        "NgrokAuthtoken": "EnterYour_NgrokAuthtoken"
"""
    __COMMANDS_LIST ="""
[quick-remote]
|Usage: self [options] [sub-options]
    |--remote                Start QuickRemote.
    |--quit                  Turn off quick-remote.
    |--timer                 Print current timer to CLI (timer start when you start the quick-remote successful).
    |    |-refresh           Refresh timer to start status.
    |    |-format '<format>' Change timer stdout format. tags: [@year, @month, @day, @hour, @minute, @second]
    |    |                   Ex: 25-2-2000
    |    |                       quick-remote --timer -format '@year/@month/@day'
    |    |                     ->2000/2/25
    |--mail                  Send mail remote to RemoteEmail.
    |    |-m '<message>'     Mail to RemoteMath with the message.
    |--clear                 Clear CLI screen.
    |--help                  Show commandS list.

    """

    __SETTINGS = None
    __TIMER = None
    __CODE_SERVER = None
    __NGROK = None
    
    def __init__(self):
        self.command = Ultities.EMPTY_STRING
        self.subcommand = Ultities.EMPTY_STRING
        self.subcommand_tail = Ultities.EMPTY_STRING
        self.__fillDataToEnvironmentVariables()
        self.__showQuickRemoteTip()

    def __showQuickRemoteTip(self):
        Bot.showRawMessage(self.__WARNING)
        Bot.showRawMessage(self.__COMMANDS_LIST)
    
    def __fillDataToEnvironmentVariables(self): 
        try:
            self.__SETTINGS = RemoteSetting()
            self.__SETTINGS.save()
            Ultities.clearQuestionMarkTTY(self.__SETTINGS.SuPassword)
            self.__TIMER = Timer.createInstanceFrom(TimeFormatMask = TimeFormatTemplates.Simple)
            #init to ngrok and code-server
            self.__CODE_SERVER = CodeServer()
            self.__NGROK = NgrokServer.createInstanceFrom(LaunchPath = self.__SETTINGS.NgrokLaunchPath, Authtoken = self.__SETTINGS.NgrokAuthtoken)
        except Exception as Except:
            Bot.showMessage(f"Settings is invalid, checkout at '{os.getcwd()}/.settings.json'", Bot.ERROR)
            Logging.Log(Except, isExit = True)
              
    @staticmethod
    def Run():
        CLI = QuickRemoteCLICommand()
        while(True):
            stdin = input()
            isSuccess = CLI.launchCommand(stdin)
            if isSuccess: Bot.showMessage(r"Successful!", Bot.SUCCESS)
            else: Bot.showMessage(r"Error or invalid input", Bot.ERROR)
            
    
    def launchCommand(self, CommandText: str):
        """False if it has except or error in process, True if not.\n
        Return type: Bool.
        """
        CommandsDictionary = self.__extractToDictionaryFrom(CommandText)
        if Ultities.isNotNone(CommandsDictionary):
            command, subcommand, subcommand_tail = self.__tearDownCommandDictionary(CommandsDictionary)
            return self.__processValidCommandCase(command, subcommand, subcommand_tail)
        else: return False

    def __tearDownCommandDictionary(self, CommandsDictionary: dict):
        command = CommandsDictionary['command']
        subcommand = CommandsDictionary['subcommand']
        subcommand_tail = CommandsDictionary['subcommand_tail']
        return command, subcommand, subcommand_tail

    def __process_remote_command(self, subcommand = Ultities.EMPTY_STRING, subcommand_tail = Ultities.EMPTY_STRING):
        self.__startServices()
        PUBLIC_URL_TUNNEL = self.__NGROK.PublicURLTunnel
        CODE_SERVER_PASSWORD = self.__CODE_SERVER.getPassword(self.__SETTINGS.SuPassword, True)
        Bot.showMessage(f'PUBLIC_URL: {PUBLIC_URL_TUNNEL}', Bot.SUCCESS)
        Bot.showMessage(f'PASSWORD__: {CODE_SERVER_PASSWORD}', Bot.SUCCESS)
        Bot.showMessage('QuickRemote has been turning on!', Bot.SUCCESS)

    def __startServices(self):
        self.__NGROK.startBackgroundAsiaTunnel(URL = self.__CODE_SERVER.BindAddress, ReadyTime = 0)
        self.__CODE_SERVER.startBackground(SudoPassword = self.__SETTINGS.SuPassword, ReadyTime = 0)
        self.__TIMER.startBackground()
            
    def __process_timer_command(self, subcommand = Ultities.EMPTY_STRING, subcommand_tail = Ultities.EMPTY_STRING):
        if subcommand == 'refresh':
            if subcommand_tail != Ultities.EMPTY_STRING: RisingException.rise('invalid command text','qr1')
            else:
                self.__refreshTimer()
                Bot.showMessage('Timer refresh success!', Bot.SUCCESS)
        elif subcommand == 'format':
            if subcommand_tail == Ultities.EMPTY_STRING: RisingException.rise('format input is empty string','qr2')
            else:
                self.__TIMER.TimeFormat = subcommand_tail
                Bot.showMessage("Update timer's time format success")
        elif subcommand == Ultities.EMPTY_STRING: self.__TIMER.showTime()

    def __refreshTimer(self):
        self.__TIMER = Timer()
        self.__TIMER.startBackground()
    
    def __process_mail_command(self, subcommand = Ultities.EMPTY_STRING, subcommand_tail = Ultities.EMPTY_STRING):
        if subcommand == 'm': Gmail.sendMessageToRemoteEmail(subcommand_tail)
        else: Gmail.sendRemoteMail(self.__NGROK, self.__CODE_SERVER)

    def __process_clear_command(self, subcommand = Ultities.EMPTY_STRING, subcommand_tail = Ultities.EMPTY_STRING):
        Ultities.clearTerminalScreen()

    def __process_quit_command(self, subcommand = Ultities.EMPTY_STRING, subcommand_tail = Ultities.EMPTY_STRING):
        self.__quit()

    def __process_help_command(self, subcommand = Ultities.EMPTY_STRING, subcommand_tail = Ultities.EMPTY_STRING):
        self.__showCommandsList()

    def __processValidCommandCase(self, command = 'help', subcommand = Ultities.EMPTY_STRING, subcommand_tail = Ultities.EMPTY_STRING):
        """ True: if command in is in quick-remote commands list and it can be launch.\n
        False: if the input command is invalid or get any exception.\n
        Return type: Bool.
        """
        IsValid = True
        try:
            if command == 'quit' and subcommand == Ultities.EMPTY_STRING: 
                self.__process_quit_command(subcommand, subcommand_tail)
            elif command == 'remote' and subcommand == Ultities.EMPTY_STRING:
                self.__process_remote_command(subcommand, subcommand_tail)
            elif command == 'clear' and subcommand == Ultities.EMPTY_STRING:
                self.__process_clear_command(subcommand, subcommand_tail)
            elif command == 'help' and subcommand == Ultities.EMPTY_STRING: 
                self.__process_help_command(subcommand, subcommand_tail)
            elif command == 'timer': self.__process_timer_command(subcommand, subcommand_tail)
            elif command == 'mail': self.__process_mail_command(subcommand, subcommand_tail)
            else: IsValid = False
        except Exception as Except:
            Logging.Log(Except)
            IsValid = False
        finally: return IsValid

    def __quit(self):
        CLIENT_DEVICE_WARNING ="""
        Force to exit the application,
        If the prcess is fine, then the
        BotMailer will send to your
        RemoteGmail a message which explain
        your local device status."""
        try: self.__turnStatusMail()
        except: Bot.showMessage("Can't send remote Mail!", Bot.ERROR)
        finally: self.__quit_force()

    def __quit_force(self):
        gc.collect()
        os._exit(os.EX_OK)

    def __turnStatusMail(self):
        SERVER_STATUS =f"""
        Server force to stop, use ssh to
        to open QuickRemote or open direcly
        in server device!!!
        {self.__TIMER.TimeText}"""
        Gmail.sendMessageToRemoteEmail(SERVER_STATUS)

    def __extractToDictionaryFrom(self, CommandText: str):
        """Extract the input command text to dictionary.\n
        Return type: Dictionary."""
        #limited 120 characters
        regexPattern = r"^(?=[a-z0-9\-]{0,120})(?:\s{0,})(?:\bself\b)\s{1,}(?:--(\w+))(?:\s+-(\w+)\s{0,}(?:'([\u0021-\u0026\u0028-\u00ff\s]+)')?)?(?:\s{0,})$"
        regexCompiler = re.compile(regexPattern, flags= re.RegexFlag.IGNORECASE & re.RegexFlag.MULTILINE)
        Groups = regexCompiler.findall(CommandText)
        if Ultities.isEmptyCollection(Groups):
            return None
        return self.__appendRawCommandsDictTo(Groups[0])

    def __appendRawCommandsDictTo(self, Groups):
        CommandsDictionary = vars(self)
        for key, index in zip(CommandsDictionary.keys(), range(len(Groups))):
            CommandsDictionary[key] = Groups[index]
        return CommandsDictionary

    def __showCommandsList(self):
        print(self.__COMMANDS_LIST)