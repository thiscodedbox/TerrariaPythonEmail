# TerrariaPythonEmail
Python script to email people when they join your Terraria server. Good for a private server with not a lot of users. I use it for my friends and I on the server we use privately. We're busy people so sometimes it's good to take a break and hop in the server when someone else happens to hop in.

**Features**
* Will only send an email every 30 minutes (prevents emails spamming out as people join/leave/join/leave/join
* Configured for TLS security on SMTP because my host required it
* Random string appended to email subject to prevent threading on gmail - makes it confusing what happened.
* Very, very, flexible - you can have this do anything in response to a console logged event on a terraria server. i.e. you could trigger an event every time the server saves, or something. Maybe have it update a web page with what is going on on the server or something.

You'll need to tee the output of your terraria server executable to a text file. I'm using wtee.exe from:

https://github.com/WinLAFS/wintee

How To Setup (Windows)

* Get Python 2.7 (wherever)
* get wtee.exe (https://github.com/WinLAFS/wintee)
* get logscanner.py (this repo)
* put in your smtp for logscanner.py and your email addresses (to and from)

example .bat script to launch terrariaserver.exe:

`cmd.exe /K "cd C:\tshock\ & TerrariaServer.exe -maxplayers 4 -world "C:\Users\Username\Documents\My Games\Terraria\Worlds\myworld.wld" --stats-optout" | c:\wtee.exe C:\tshock\logs\tlivelog.txt`

example shortcut to logscanner.py

`C:\Python27\python.exe c:\tshock\logscanner.py`
