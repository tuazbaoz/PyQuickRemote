- [Index:](#index)
- [About Quick Remote](#about-quick-remote)
- [Usecase Diagram](#usecase-diagram)
- [Commands](#commands)
- [Quick Remote Settings](#quick-remote-settings)
  - [Precondition:](#precondition)
    - [Contact: horrorplus0099@gmail.com](#contact-horrorplus0099gmailcom)

## Index:

## About Quick Remote

QuickRemote allows can using visual studio code remote from a public url.

Now you can use your VS-Code in any internet browser as your internal machine.

## Usecase Diagram

![quick remote usecase diagram](https://github.com/tuazbao-heo/ImageHosting/blob/ea5d4c6ef9994e67e94917b35b0771b8b794796f/08FF8362-C0C7-426B-8649-268881C093CD.jpeg?raw=true "Quick remote usecase diagram")

## Commands

```bash
[quick-remote] |Usage: self [options] [sub-options]
|--remote Start QuickRemote.
|--quit Turn off quick-remote.
|--timer Print current timer to CLI (timer start when you start the quick-remote successful).
| |-refresh Refresh timer to start status.
| |-format '<format>' Change timer stdout format. tags: [@year, @month, @day, @hour, @minute, @second]
| | Ex: 25-2-2000
| | quick-remote --timer -format '@year/@month/@day'
| | ->2000/2/25
|--mail Send mail remote to RemoteEmail.
| |-m '<message>' Mail to RemoteMath with the message.
|--clear Clear CLI screen.
|--help Show commandS list.
```

Example:

`self --remote`  
output:

```
BOT_SUCCESSOR: PUBLIC_URL: http://example.quickremote.io
BOT_SUCCESSOR: PASSWORD\_\_: 380f8f8b58741547ada080dc
BOT_SUCCESSOR: QuickRemote has been turning on!
BOT_SUCCESSOR: Successful!
```

`self --timer`  
output:

```
Timer: Hour:0 - Minute:5 - Second:15
BOT_SUCCESSOR: Successful!
```

## Quick Remote Settings

Create a JSON file name `.settings.json` and complete your settings follow the below termplate:

```json
{
  "BotGmail": "example@gmail.com",
  "BotGmailPassword": "example@123456",
  "SuPassword": "Your_SudoPassword",
  "RemoteEmail": "Your_Email_Which_Get_The_Message_From_Bot_Gmail@gmail.com",
  "NgrokLaunchPath": "/ngrokDirectory/ngrok"
}
```

### Precondition:

1.  Run the program on Linux OS/ WSL only.
2.  Install code-server and ngrok on your machine.
3.  Authorized ngrok account.
4.  Installed ngrok web api.

#### Contact: horrorplus0099@gmail.com
