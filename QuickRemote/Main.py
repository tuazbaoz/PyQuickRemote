from QuickRemoteCLICommand import QuickRemoteCLICommand as QuickRemoteCLI
from Logging import Logging
from Settings import RemoteSetting
import Ultities

#pre-conditions:
#   + Run the program on Linux OS/ WSL only.
#   + Install code-server and ngrok.
#   + Authorized ngrok account on your machine.
#   + Installed ngrok web api.

#QuickRemote allows can using visual studio code
#remote from a public url.

def main():
    """run QuickRemote CLI Command"""

    #       h   h   e e e   o o o
    #       h   h   e       o   o
    #       h h h   e e e   o   o
    #       h   h   e       o   o
    #       h   h   e e e   o o o

    #run quick remote as console app.
    QuickRemoteCLI.Run()
    pass

#perform
main()
    
 