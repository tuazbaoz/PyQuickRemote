import Ultities
import requests as req
import sys
import _thread
from os import path
from Logging import Logging
from Bot import Bot
from RisingException import RisingException

class NgrokServer:
    def __init__(self, LaunchPath: str, Authtoken: str):
        if not path.isfile(LaunchPath):
            RisingException.rise('ngrok launch path is not existed', 'ns1')
        self.__LaunchPath = LaunchPath
        self.__Authtoken = Authtoken
    
    __API_REST_URL = 'http://localhost:4040'
    __API_TUNNEL = '/api/tunnels'
    __ASIA_SERVER_TUNNEL_SUBCOMMAND_TEXT = '-region ap'
    __LOG_TO_SHELL_SUBCOMMAND_TEXT = '-log=stdout'
    
    @property
    def LaunchPath(): pass 
    @LaunchPath.setter
    def LaunchPath(self, Path: str):
        if path.isfile(Path): self.__LaunchPath = Path
        else: RisingException.rise('ngrok launch path is not existed', 'ns1')
    @LaunchPath.getter
    def LaunchPath(self):
        return self.__LaunchPath

    @property
    def Authtoken(): pass
    @Authtoken.getter
    def Authtoken(self):
        return self.__Authtoken

    @property
    def PublicURLTunnel(): pass
    @PublicURLTunnel.getter
    def PublicURLTunnel(self):
        return self.__getPublicURLTunnel()

    @property
    def Command(): pass
    @Command.getter
    def Command(self): return self.__Command

    #behaviors
    def __getPublicURLTunnel(self):
        """Get public URL tunnel from a ngrok response.\n
        Return type: String.
        """
        LimitedRequestTime = 5
        response = self.__getTunnelReponse(LimitedRequestTime)
        if Ultities.isNotNone(response):
            jsonf = response.json()
            if Ultities.isEmptyCollection(jsonf):
                RisingException.rise('Response is empty collection.', 'ns4')
            URL = jsonf['tunnels'][0]['public_url']
            return URL
        else: RisingException.rise('Response is None or Empty collection', 'ns2')

    def __getTunnelReponse(self, TimoutLimitedRemain = 1) -> req.Response:
        """Get response tunnel from web api,
        limited 5 times to timeout limited.\n
        Return type: Response object.
        """
        try:
            response = req.get(f'{self.__API_REST_URL}{self.__API_TUNNEL}', timeout = 0.01)
            return response
        except req.RequestException as Except:
            if TimoutLimitedRemain == 0: RisingException.rise('Request timeout out of limit', 'ns3')
            else:
                Bot.showMessage(f'{TimoutLimitedRemain} request timeout time remaining', Bot.ERROR)
                TimoutLimitedRemain = TimoutLimitedRemain - 1
                self.__getTunnelReponse(TimoutLimitedRemain)
    
    @staticmethod
    def createInstanceFrom(LaunchPath: str, Authtoken: str):
        return NgrokServer(LaunchPath, Authtoken= Authtoken)

    #ngrok behaviors
    def startBackgroundAsiaTunnel(self, URL: str, ReadyTime = 1):
        """Start background tunnel to the URL with ReadTime.
        """
        Lock = _thread.allocate_lock()
        Ultities.startNewThreadFrom(Lock, self.__startAsiaTunnel, URL, ReadyTime)
        
    def __startAsiaTunnel(self, URL, ReadyTime = 1):
        Ultities.Wait(ReadyTime)
        StartTunnelCommand = f' http {self.__ASIA_SERVER_TUNNEL_SUBCOMMAND_TEXT} {self.__LOG_TO_SHELL_SUBCOMMAND_TEXT} {URL}'
        self.__callSubprocess(StartTunnelCommand)
    
    def __callSubprocess(self, Command: str):
        """Match ngrok's launch-path and process the subprocess Command.
        """
        LaunchCommand = f'{self.LaunchPath} {Command}'
        LaunchCommand = Ultities.appendAssignToNullCommand(LaunchCommand)
        Ultities.callSubprocess(LaunchCommand)
        
    def authorize(self):
        """Authorize the ngrok user from the authtoken in
        Json settings file [.settings.json].
        """
        Command = f'authorize {self.Authtoken}'
        self.__callSubprocess(Command)
    
    def install_Web_API(self):
        """Install web API by "curl" command, ngrok open [http://localhost:4040] as 
        web api. Browse the URL to monitor your ngrok accessing.
        """
        Command = f'curl {self.__API_REST_URL}/api'
        Ultities.callSubprocess(Command)