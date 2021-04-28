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
                    <li><a href="#quickremote-settings">Settings</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <!-- intro part -->
            <section id="about">
                <h2>About Quick Remote</h2>
                <article>
                    <p>
                    Can launch the Program on Linux OS/ WSL only.<br>
                    QuickRemote allows clients can launch Ngr*k and C*de-server at the same time, display Ngr*k public URL and C*deServer password, mail to remote Email...
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
                    <img src="https://github.com/tuazbao-heo/ImageHosting/blob/Master/QuickRemoteUseCase.jpg?raw=true" alt="quick remote usecase diagram" title="Quick remote usecase diagram" width="520" height="600">
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
                        |--timer                 Print current timer to CLI once.<br>
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
                    ->Ngr*k Public URL      :xxxxxxxxxxxxxxxxxx<br>
                    ->C*deServer Password :xxxxxxxxxxxxxxxxxxxx<br><br>
                    <code>self --timer</code><br>
                    output:<br>
                    Timer<br>
                    ==========================<br>
                        Year    : 0<br>
                        Month   : 0<br>
                        Day     : 0<br>
                        Hour    : 0<br>
                        Minute  : 3<br>
                        Second  : 45<br>
                    ==========================<br>
                </p>
            </section>
            <!-- QuickRemote settings -->
            <section id="settings">
                <h2>QuickRemote Settings</h2>
                <!-- JSON settings -->
                <article>
                    <p>
                        Create a JSON file name <code>.settings.json</code> and complete your settings follow below term:<br>
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
                        <li>installed ngrok</li>
                        <li>installed code-server</li>
                        <li>corrected setting fields</li>
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
