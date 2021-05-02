import json
import os
import Ultities
from RisingException import RisingException
from Bot import Bot

#this class might be inhertances
class Settings(object):
    def __init__(self):
        """This object launch first"""
        # #setting fieds as class attributes
        # #self.attribute = 'value'

    __SETTINGS_FILE_NAME = r'.settings.json'

    #behaviors
    def __addSetting(self, Name: str, value: str):
        setattr(self, Name, value)
    
    def __loadSettingsFrom(self, Settings: dict):
        SafeSettingKeys = vars(self).keys()
        for Atrribute in SafeSettingKeys:
            Value = Ultities.EMPTY_STRING
            if Atrribute in Settings: Value = Settings[Atrribute]
            self.__addSetting(Atrribute, Value)

    def load(self):
        """Load all settings of [.settings.json] to this Settings instance.
        """
        if os.path.isfile(self.__SETTINGS_FILE_NAME):
            with open(self.__SETTINGS_FILE_NAME, mode = 'r') as file:
                jSettings = json.loads(file.read())
                self.__loadSettingsFrom(jSettings)

    def save(self):
        """Save the current settings to [.settings.json].
        """
        Settings = vars(self)
        with open(self.__SETTINGS_FILE_NAME, mode = 'w') as file:
            jSettings = json.dumps(Settings, indent= 1)
            file.write(jSettings)


class RemoteSetting(Settings):
    def __init__(self):
        """for each public field in this class is a setting row,
        add a new public field to add your new setting row.
        """
        self.BotGmail = Ultities.EMPTY_STRING
        self.BotGmailPassword = Ultities.EMPTY_STRING
        self.SuPassword = Ultities.EMPTY_STRING
        self.RemoteEmail = Ultities.EMPTY_STRING
        self.NgrokLaunchPath = Ultities.EMPTY_STRING
        self.NgrokAuthtoken = Ultities.EMPTY_STRING
        self.load()
        self.__checkSettingFields()

    def __checkSettingFields(self):
        self.__displayEmptySettings()
        if not Ultities.isValidSudopassword(self.SuPassword):
            RisingException.rise('Invalid sudo password in settings file', 'rs1')

    def __isExistedEmptySetting(self):
        Keys = vars(self)
        ExistedKey = [key for key in keys if keys[key] != Ultities.EMPTY_STRING]
        return Ultities.isNone(ExistedKey)

    def __getEmptySettings(self):
        """get all empty settings collection."""
        Settings = vars(self)
        return [key for key in Settings if Settings[key] == Ultities.EMPTY_STRING]

    def __displayEmptySettings(self):
        """stdout of remoteSettings
        this display one by one missing settings"""
        EmptySettingKeys = self.__getEmptySettings()
        if not Ultities.isEmptyCollection(EmptySettingKeys):
            Bot.showMessage("Exist empty settings, which can lead this application to crashes/errors", Bot.ERROR)
            for key in EmptySettingKeys:
                Bot.showMessage(f"{key} is empty", Bot.ERROR)

