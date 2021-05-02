import smtplib
import email
import Ultities
from Bot import Bot
from NgrokServer import NgrokServer
from CodeServer import CodeServer
from Settings import RemoteSetting
from RisingException import RisingException

class MailSubjectTemplates:
    Type1 = """BotMailer: Hello, I take this from Heo!! it's for you!!!"""
    Type2 = """BotMailer: Mail from Heo to Heo!!!"""
    Type3 = """BotMailer: here is your Visual Studio Code remote, lets get it!!!"""
    Type4 = """BotMailer: Heo Heo Heo Heo Heo Heo Heo Heo Heo Heo Heo Heo!!!"""
    
class Gmail:
    def __init__(self, 
                USER_GMAIL = 'example@gmail.com',
                USER_PASSWORD = 'example@123456',
                SEND_FROM = 'example',
                SEND_TO = 'destination.mail@gmail.com'):

        if USER_GMAIL == Ultities.EMPTY_STRING: RisingException.rise('user_gmail is empty string','g1')
        if USER_PASSWORD == Ultities.EMPTY_STRING: RisingException.rise('user_password is empty string', 'g2')
    
        self.__UserGmail = USER_GMAIL
        self.__UserPassword = USER_PASSWORD
        self.SendFrom = SEND_FROM
        self.SendTo = SEND_TO


    def SendMail(self, Subject: str, Text: str):
        """Send a mail to destnation-Email [send_to].
        """
        msg = self.__groupMessageFrom(self.SendTo, Subject, Text)
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(self.__UserGmail, self.__UserPassword)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())   
        server.close()

    def __groupMessageFrom(self, ToEmail: str, Subject: str, Text: str):
        msg = email.message.Message()
        msg['Subject'] = Subject
        msg['From'] = self.SendFrom
        msg['To'] = self.SendTo
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(Text)
        return msg

    @staticmethod
    def sendRemoteMail(Ngrok: NgrokServer, CodeServer: CodeServer):
        """Send remote mail to destionation mail in [.settings.json].
        """
        Settings = RemoteSetting()
        Mailer = Gmail.createInstanceFrom(USER_GMAIL = Settings.BotGmail, USER_PASSWORD = Settings.BotGmailPassword,
                                        SEND_FROM = Ultities.getUsername(), SEND_TO = Settings.RemoteEmail)
        Subject = MailSubjectTemplates.Type2
        PublicURL = Ngrok.PublicURLTunnel
        CodeSeverPassword = CodeServer.getPassword(SudoPassword = Settings.SuPassword, isRoot = True )
        simpleVSCodeRemoteMessage = Gmail.getSimpleVSRemoteMessage(PublicURL, CodeSeverPassword)  
        Mailer.SendMail(Subject, simpleVSCodeRemoteMessage)
        Bot.showMessage('Mail has been sent', Bot.SUCCESS)

    
    @staticmethod
    def sendMessageToRemoteEmail(Message: str):
        """Send normal message to destination email in [.settings.json].
        """
        Settings = RemoteSetting()
        Mailer = Gmail.createInstanceFrom(USER_GMAIL = Settings.BotGmail, USER_PASSWORD = Settings.BotGmailPassword,
                                        SEND_FROM = Ultities.getUsername(), SEND_TO = Settings.RemoteEmail)
        Subject = MailSubjectTemplates.Type2
        Mailer.SendMail(Subject,Message)
        Bot.showMessage('Mail has been sent', Bot.SUCCESS)
            
    @staticmethod
    def createInstanceFrom(USER_GMAIL: str, USER_PASSWORD: str, SEND_FROM: str, SEND_TO: str):
        return Gmail(USER_GMAIL, USER_PASSWORD, SEND_FROM, SEND_TO)

    @staticmethod
    def getSimpleVSRemoteMessage(Url: str, Password: str):
        Html = f"""<!DOCTYPE html><html><body><h2 style="text-align: center;">VISUAL STUDIO CODE REMOTE</h2><table style="width:100%"><tr><th>URL</th><td>{Url}</td></tr><tr><th>PASSWORD</th><td>{Password}</td></tr></table></body></html>
                """
        return Html