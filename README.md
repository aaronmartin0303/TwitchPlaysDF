TwitchPlaysDF
=============

Exactly what it says! From <a href='https://github.com/sunshinekitty5/TwitchPlaysPokemon'>Sunshinekitty5's TwitchPlaysPokemon</a>


<h1>Twitch Plays Dwarf Fortress IRC Bot</h1>
<h2>Written in Python 3.3.4</h2>
<p>This is a quick and easy way for people Windows 7, Python33, and win32 to connect Twitch to Dwarf Fortress and have an interactive chat.</p>

<h2>Prerequisites</h2>
<p>This is written in Python 3.3.4 and meant to run on Windows, it has only been tested on Windows 7 because I hate Windows 8.  That being said, you need to install this:

<a href="http://www.python.org/ftp/python/3.3.4/python-3.3.4.amd64.msi">64 bit</a>

<a href="http://www.python.org/ftp/python/3.3.4/python-3.3.4.msi">Everyone else</a>

After that install this:

<a href="http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/pywin32-218.win-amd64-py3.3.exe/download">64 bit</a>

<a href="http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/pywin32-218.win32-py3.3.exe/download">Everyone Else</a>

You'll want to download <a href="http://www.bay12games.com/dwarves/">Dwarf Fortress</a>!  I haven't tried this with the PeridaxisErrant's excellent Lazy Newb Pack, just vanilla installation.  WARNING: Make a separate install or else people could abandon your forts. :(

Now you're good, download and clone <a href="https://github.com/aaronmartin0303/TwitchPlaysDF">this</a>; don't re-arrange or re-name the contents without changing the scripts, you will also need to update ircbot.py to connect to your account, or else it will NOT work.

<h2>How-to run</h2>

<p>Of course update ircbot.py with your credentials first

If you have Python33 installed correctly, you can just double click the ircbot.py first, and after it establishes it is connected, open up controller.py.

However, if you need to do things with command line:

Open up two COMMAND PROMPTS and before running the programs type in chcp 65001 into EACH

First start the ircbot, verify that it echoes "Connected" to the channel and can receive messages, then start the controller.py which will open VBA as well as focus it every 3 seconds when it needs to make a command.

(To people who don't know command line, navigate to the directory your stuff is located in with cd Directory\Name then type in the name of the program, if you installed Python 3.3.4 correctly it will start the program)


<h2>In other news</h2>
Now I will shamelessly plug sunshinekitty5's (the creator of the Pokemon bot, that I adapted for DF) channel <a href="http://www.twitch.tv/nutz1"><b>HERE</b></a>

However once he moves it to a server it will be shown <a href="http://www.twitch.tv/twitchplaysgameboyadvance"><B>HERE</B></a>

Go here for occasional <a href='http://www.twitch.tv/aaichabod'>TWITCH PLAYS DWARF FORTRESS: ADVENTURE MODE!</a>

<h3>Side:</h3>
I'm just learning the basics of Python, so let's fork and merge and make a better bot!
