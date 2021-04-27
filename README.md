<!DOCTYPE html>
<html>
    <head>
        <title>Quick-Remote</title>
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
                    <li><a href="#about" >About Quick Remote</a></li>
                    <li><a href="#diagram" >Usecase Diagram</a></li>
                    <li><a href="#commands" >Commands</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <section id="about">
                <h3>About Quick Remote:</h3>
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
            <section id="diagram">
               <h3>Usecase Diagram:</h3>
               <figure>
                    <img src="https://github.com/tuazbao-heo/ImageHosting/blob/Master/QuickRemoteUseCase.jpg?raw=true" alt="quick remote usecase diagram" title="Quick remote usecase diagram" width="520" height="600">
               </figure>
            </section>
            <section id="commands">
                <h3>Commands:</h3>
                <article>
                    <code>
                        [quick-remote]<br>
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
                            |--help                  Show commandS list.
                    </code>
                    <p>Example:</p>
                    <code>
                        self --remote<br>
                            ->Ngr*k Public URL      :xxxxxxxxxxxxxxxxxx<br>
                            ->C*deServer Password :xxxxxxxxxxxxxxxxxxxx
                    </code>
                </article>
            </section>
        </main>
        <!-- footer -->
        <footer>
            <small><br><br>Contact: horrorplus0099@gmail.com</small>
        </footer>
    </body>
</html>
