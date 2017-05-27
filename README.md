# TerrariaPythonEmail
Python script to email people when they join your Terraria server.

You'll need to tee the output of your terraria server executable to a text file. I'm using wtee.exe from:

https://github.com/WinLAFS/wintee

How To:

Setup (my setup is Windows Server 2008 R2)

* Get Python 2.7 (wherever)
* get wtee.exe (https://github.com/WinLAFS/wintee)
* get logscanner.py (this repo)
* put in your smtp for logscanner.py and your email addresses (to and from)



example .bat script to launch terrariaserver.exe:

`cmd.exe /K "cd C:\tshock\ & TerrariaServer.exe -maxplayers 4 -world "C:\Users\username\Documents\My Games\Terraria\Worlds\myworld.wld" --stats-optout" | c:\wtee.exe C:\tshock\logs\tlivelog.txt`

example shortcut to logscanner.py

`C:\Python27\python.exe c:\tshock\logscanner.py`
