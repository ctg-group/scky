
from core.colors import *

help_message=f"""

  {R}| SCKY HELP MENU{N}
    {Y}shutdown{N}  - Shutdowns server, but client be checking for server is open every 5 seconds.
    {Y}msgbox [title] [message] [icon]{N} - Shows messagebox to victim with TITLE and MESSAGE.
    	ICON - 1: OK, 2: Error, 3: Question, 4: Information.
    {Y}screenshot{N} - Takes screenshot of victim's screen.
    {Y}sendfile [path]{N} - Send's file to victim.
    {Y}runcmd [command]{N} - Runs's command (command line) to victim. (No response)
    {Y}runcode_nocallback [python code]{N} - Run's python code in victim. (WARNING: It's uses by try-except exec!)
    {Y}runcode_callback [python code]{N} - Run's python code in victim, and returns result.(Success or error, need  to wait for response!)

  {Y}| Additional Information{N}
    For spaces in one argument use "", example:
    	msgbox "Hello, everybody!" "Whats it is???" 3
    	sendfile "C:\My documents\file.exe"
    We not responsible for you actions!

  {G}| Developers{N}
    Developed by {R}CTG.
    (g) CTG. 2021 | All copyright are reserved!
"""

menu=f"""
      {R}1.{G} Build Backdoor     {R}4.{G} Authors
      {R}2.{G} Show Sessions      {R}5.{G} Information
      {R}3.{G} Open Session (ID)  {R}6.{G} Load Last Session
                                                              {R}0.{G} Exit{N}
"""