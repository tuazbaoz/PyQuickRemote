<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <!-- header -->
        <header>
            <h1>Quick Remote</h1>
            <h2>Index:</h2>
            <!-- navigations -->
            <nav>
                <ul>
                    <li><a href="#about-quick-remote" >About Quick Remote</a></li>
                    <li><a href="#usecase-diagram" >Usecase Diagram</a></li>
                    <li><a href="#commands" >Commands</a></li>
                    <li><a href="#quick-remote-settings">Settings</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <!-- intro part -->
            <section id="about">
                <h2>About Quick Remote</h2>
                <article>
                    <p>
                        QuickRemote allows can using visual studio code remote from a public url.
                        <aside>
                            Now you can use your VS-Code in any internet browser as your internal machine.
                        </aside>
                    </p>
                </article>
            </section>
            <!-- usecase figure -->
            <section id="diagram">
               <h2>Usecase Diagram</h2>
               <figure>
                    <img src="https://github.com/tuazbao-heo/ImageHosting/blob/ea5d4c6ef9994e67e94917b35b0771b8b794796f/08FF8362-C0C7-426B-8649-268881C093CD.jpeg?raw=true" alt="quick remote usecase diagram" title="Quick remote usecase diagram" width="520" height="600">
               </figure>
            </section>
            <!-- commands part -->
            <section id="commands">
                <!-- command overview -->
                <h2>Commands</h2>
                <p>
                    [quick-remote]
                    |Usage: self [options] [sub-options]<br>
                        |--remote                Start QuickRemote.<br>
                        |--quit                  Turn off quick-remote.<br>
                        |--timer                 Print current timer to CLI (timer start when you start the quick-remote successful).<br>
                        |    |-refresh           Refresh timer to start status.<br>
                        |    |-format '<format>' Change timer stdout format. tags: [@year, @month, @day, @hour, @minute, @second]<br>
                        |    |                   Ex: 25-2-2000<br>
                        |    |                       quick-remote --timer -format '@year/@month/@day'<br>
                        |    |                     ->2000/2/25<br>
                        |--mail                  Send mail remote to RemoteEmail.<br>
                        |    |-m '<message>'     Mail to RemoteMath with the message.<br>
                        |--clear                 Clear CLI screen.<br>
                        |--help                  Show commandS list.<br>
                </p>
                <!-- example of commonly commands -->
                <p>Example:</p>
                <p>
                    <code>self --remote</code><br>
                    output:<br>
                    BOT_SUCCESSOR: PUBLIC_URL: http://example.quickremote.io<br>
                    BOT_SUCCESSOR: PASSWORD__: 380f8f8b58741547ada080dc<br>
                    BOT_SUCCESSOR: QuickRemote has been turning on!<br>
                    BOT_SUCCESSOR: Successful!<br><br>
                    <code>self --timer</code><br>
                    output:<br>
                    Timer: Hour:0 - Minute:5 - Second:15<br>
                    BOT_SUCCESSOR: Successful!<br><br>
                </p>
            </section>
            <!-- QuickRemote settings -->
            <section id="settings">
                <h2>Quick Remote Settings</h2>
                <!-- JSON settings -->
                <article>
                    <p>
                        Create a JSON file name <code>.settings.json</code> and complete your settings follow the below termplate:<br>
                        <em>{<br>
                        "BotGmail": "example@gmail.com",<br>
                        "BotGmailPassword": "example@123456",<br>
                        "SuPassword": "Your_SudoPassword",<br>
                        "RemoteEmail": "Your_Email_Which_Get_The_Message_From_Bot_Gmail@gmail.com",<br>
                        "NgrokLaunchPath": "/ngrokDirectory/ngrok",<br>
                        }</em>
                    </p>
                </article>
                <aside>
                    <!-- precondition -->
                    <h3>Precondition:</h3>
                    <ol>
                        <li>Run the program on Linux OS/ WSL only.</li>
                        <li>Install code-server and ngrok on your machine.</li>
                        <li>Authorized ngrok account.</li>
                        <li>Installed ngrok web api.</li>
                    </ol>
                </aside>
            </section>
        </main>
        <!-- footer -->
        <footer>
            <br><br>
            <small>Contact: horrorplus0099@gmail.com</small>
        </footer>
    </body>
</html>
