
"""
  Scky - Windows remote backdoor-based botnet.
         Developed by CTG group.
"""

import time
import sys
from core.colors import *
import misc.logos
import misc.messages
import core.utils
import core.builder
import core.Sessions.utils
import core.Sessions.Connection

class Main:
      
  def ShowMenu():
    print(misc.messages.menu)
  
  def ShowAuthors():
    print(misc.logos.logo)
    print(f'    {C}DEVELOPED BY {R}C{Y}T{G}G{C} GROUP!')
    print(f'    {G}V1.4{N}')
    print(f'    {R}Thanks to FTDOT (t.me/h4x0rdd){N}')
    print(f'    {C}OFFICIAL CTG GROUP TELEGRAM: t.me/joinchat/Wm8qHlrgfMlhMDgy (its working to next SCKY update!){N}')
  
  def ShowInformation():
    print(misc.logos.logo)
    print(f'    V1.4, SCKY backdoor software.')
    print(f'    Modules: Sessions,win_deleter by ftdot, folder "modules" - is v1.5 update feature!')
    print(f'    License:')
    with open('license.txt','r') as f: license_=f.read()
    print(license_)
    time.sleep(3)
    
  def GetMenuKey():
    p=f' {G}S C K Y {R}> {N}'
    inp=input(p)
    if inp in '1234560' and len(inp)==1:return inp
    else:return 'no-option'
    
  def MenuKeyHandle(key):
    if key=='1':core.builder.BuildBackdoor()
    elif key=='2':core.Sessions.utils.ShowSessions()
    elif key=='3':core.Sessions.utils.OpenSessionByID()
    elif key=='4':Main.ShowAuthors()
    elif key=='5':Main.ShowInformation()
    elif key=='6':core.Sessions.utils.LoadLastSession()
    elif key=='0':sys.exit()
    else:print(f'[{R}-{N}] This key not binded!')
      
if __name__=="__main__":
  core.utils.clear()
  print(misc.logos.logo)
  while True:
    Main.ShowMenu()
    key=Main.GetMenuKey()
    Main.MenuKeyHandle(key)