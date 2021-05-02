import yaml
import _thread
import time
import subprocess
import getpass
import os
from Logging import Logging
from Bot import Bot

def getUsername() -> str:
    """Get current username from the evironment.\n
    Return type: string.
    """
    return getpass.getuser()

def isValidSudopassword(Password: str) -> bool:
    """Check the input password is sudo or not.\n
    Return type: Bool.
    """
    Command = f'(echo {Password} | sudo -S -v)'
    Command = appendAssignToNullCommand(Command)
    try:
        subprocess.check_call(Command, shell=True)
        return True
    except subprocess.CalledProcessError as Except:
        return False
    

def getYamlObject(path: str) -> yaml.YAMLObject:
    """Get yaml from the file path.\n
    Return type: Yaml object.
    """
    YamlFile = open(path)
    return yaml.safe_load(YamlFile)

def getYamlObjectRoot(path: str, SudoPassword: str) -> yaml.YAMLObject:
    """Get yaml from the file path as Root.\n
    Return type: Yaml object.
    """
    Command = f'cat {path}'
    Command = appendPasswordAsRootCommand(Command, SudoPassword)
    Output = callSubprocess(Command, True)
    return yaml.safe_load(Output)

def callSubprocess(Command: str, isCheckout = False, shell = True):
    """Calls Command as subprocess.\n
    isCheckout [Bool]: returns [String] stdout after processed the Command.\n
    shell [Bool]: processes the Command in current terminal.
    """
    if isCheckout: return subprocess.check_output(Command, shell=shell)
    else: subprocess.run(Command, shell=shell)


def startNewThreadFrom(Lock, Function, *arg):
    """Start new thread, the thread calls the function wth given arguments\n
    from the tupple arg. The function also runs inside the Lock to avoid deadlock.
    """
    if(Lock.locked):
        Lock.acquire()
        _thread.start_new_thread(Function,arg)
        Lock.release()

def clearQuestionMarkTTY( SudoPassword: str):
    """Clears Question marks as hidden terminal processes.
    """
    Command = "kill $(ps aux | grep '?' | awk '{print $2}')"
    Command = appendPasswordAsRootCommand(Command, SudoPassword)
    Command = appendAssignToNullCommand(Command)
    callSubprocess(Command)
    
def clearTerminalScreen():
    callSubprocess('clear')

def printCurrentDirectory():
    callSubprocess('pwd')

def appendPasswordAsRootCommand(Command: str, Password: str) -> str:
    """Pipe 'process as SUDO' Command to the given Command.\n
    Password might is a correct Sudopassword.\n
    Return type: String.
    """
    suffix = f"echo {Password} | sudo -S "
    __Command = f'{suffix}{Command}'
    return __Command

def appendAssignToNullCommand(Command: str) -> str:
    """pipe the given string Command with assign to null Command\n
    Return type: String
    """
    return f'{Command} > /dev/null'
    
def roundLeft(value: float):
    return round(value - 0.5)
    
def Wait(DelayTime: int):
    time.sleep(DelayTime)
    
def keepRunning():
    while True: 
        key = input()
        print(key)

def isNone(Value):
    return Value == None

def isNotNone(value):
    return value != None

def isEmptyCollection(value):
    return len(value)==0
    
#public variables
EMPTY_STRING = ''
