import Ultities
import _thread

class CodeServer:
    def __init__(self):
        self.__OS_Username = Ultities.getUsername()

    __COMMAND = 'code-server'
    __CONFIG_PATH =  '/.config/code-server/config.yaml'
    __HTTP_SERVER_URL = 'http://127.0.0.1:8080'

    @property
    def BindAddress():pass
    @BindAddress.getter
    def BindAddress(self):
        Config = self.__getYamlConfigFile()
        return Config['bind-addr']
    
    @property
    def BindURL():pass
    @BindURL.getter
    def BindURL(self):
        return f'http://{self.BindAddress}'
            
    #behaviors
    def getPassword(self, SudoPassword: str, isRoot = False) -> str:
        """get code-server password. Provide correct Sudopassword and 
        set isRoot == True to get the code-server root password.\n
        Return type: String.
        """
        if isRoot: return self.__getPasswordFromRootConfig(SudoPassword)
        return self.__getPasswordFromConfig()

    def getConfigPath(self, isRoot = False) -> str:
        """Get code-server config path, set isRoot == True to get code-server's
        Config root Path.\n
        Return type: String."""
        if isRoot: return self.__getRootConfigPath()
        return self.__getNormalUserConfigPath()
    
    def __getNormalUserConfigPath(self):
        HomeDirectory = f'/home/{self.__OS_Username}'
        return f'{HomeDirectory}{self.__CONFIG_PATH}'

    def __getRootConfigPath(self): 
        return f'/root{self.__CONFIG_PATH}'
    
    def __getYamlConfigFile(self, SudoPassword = Ultities.EMPTY_STRING, isRoot = False):
        ConfigPath = self.getConfigPath(isRoot)
        if(isRoot): return Ultities.getYamlObjectRoot(path = ConfigPath, SudoPassword = SudoPassword)
        return Ultities.getYamlObject(ConfigPath)

    def __getPasswordFromConfig(self):
        config = self.__getYamlConfigFile()
        return config['password']

    def __getPasswordFromRootConfig(self, SudoPassword: str):
        config = self.__getYamlConfigFile(SudoPassword, isRoot = True)
        return config['password']

    #Commands
    def startBackground(self, SudoPassword: str, ReadyTime = 1):
        Lock = _thread.allocate_lock()
        Ultities.startNewThreadFrom(Lock, self.start, SudoPassword, ReadyTime)

    def start(self, SudoPassword: str, ReadyTime = 1):
        Ultities.Wait(ReadyTime)
        Command = Ultities.appendPasswordAsRootCommand(self.__COMMAND, SudoPassword)
        Command = Ultities.appendAssignToNullCommand(Command)
        Ultities.callSubprocess(Command)