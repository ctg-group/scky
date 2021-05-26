
from core.colors import *
from .sessions import *

def last_session():
  sessions=Session.load_sessions_('.last_session')
  if len(sessions)==0:return None
  else:return sessions[0]

def ShowSessions():
  sessions=Session.load_sessions()
  print(f'\n{R} ALL SESSIONS:{N}')
  if len(sessions)==0:
    print(f'    {R}Not have avaible sessions!')
  for s in sessions:
    sid=s.id
    sdn=s.display_name
    print(f'    {G}ID:{sid} DISPLAY NAME: {sdn}{N}')

def OpenSessionByID():
  sessions=Session.load_sessions()
  print(f'\n{R}INPUT ID OF SESSION FOR OPEN.{N}')
  p=f' {G}S C K Y \ S E S S I O N {R}> {N}'
  while True:
    inp=input(p)
    try:_=int(inp)
    except:print(f'[{R}-{N}] ENTER NUMBER!')
    for s in sessions:
      if s.id==int(inp):
        with open('.last_session','w+') as f:f.write('')
        s.save_('.last_session')
        s.conn.EnterController()
        break

def LoadLastSession():
  ls_ = last_session()
  if ls_!=None:Session.conn.EnterController()
  else:print('No last session!')