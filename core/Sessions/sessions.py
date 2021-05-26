import pickle
import os
from .Connection import *
class Session:
  def __init__(self, display_name, conn):
    self.display_name = display_name
    self.conn = conn
    self.id = conn.id
  
  def load_sessions():
    if os.path.exists('.sessions') and os.path.isfile('.sessions'):
      f=open('.sessions','r')
      sessions=[]
      sess=f.read()
      if len(sess)<2:
        return sessions
      for l in sess.split('\n'):
        opts=l.split(':')
        sessions.append(Session(opts[0],Connection(opts[1],int(opts[2]),int(opts[3]))))
      f.close()
      return sessions
    else:
      f=open('.sessions','w+')
      f.close()
      return []
  
  def load_sessions_(fn):
    if os.path.exists(fn) and os.path.isfile(fn):
      f=open(fn,'r')
      sessions=[]
      if len(f.read())<2:return sessions
      for l in f.read():
        opts=l.split(':')
        sessions.append(Session(opts[0],Connection(opts[1],opts[2],opts[3])))
      f.close()
      return sessions
    else:
      f=open(fn,'w+')
      f.close()
      return []

  def save(self):
    sessions = [f'{self.display_name}:{self.conn.bind_ip}:{self.conn.bind_port}:{self.conn.id}']
    with open('.sessions','r') as f:
      if not len(f.read())<2:
        for l in f.read():
          sessions.append(l)
    f = open('.sessions', 'w')
    r=''
    for s in sessions:r+=s
    f.write(r)
    f.close()
  
  def save_(self,fn):
    sessions = [f'{self.display_name}:{self.conn.bind_ip}:{self.conn.bind_port}:{self.conn.id}']
    with open(fn,'r') as f:
      if not len(f.read())<2:
        for l in f.read():
          sessions.append(l)
    f = open(fn, 'w')
    r=''
    for s in sessions:r+=s
    f.write(r)
    f.close()