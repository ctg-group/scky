#@OBFUSCATED,PYOBUF,BY FTDOT
import os as A_0388
from base64 import b64decode as A_0389
import sys as A_0390
S_0390=__name__;S_0392=A_0389('X19tYWluX18=').decode()
S_0393='y';S_0396='wb'
B_0390=b'';F_0031=input
F_0032=print;F_0375=A_0388.path.exists
F_0376=A_0388.rmdir;F_0386=A_0388.listdir
F_0387=A_0388.path.join;F_0388=A_0388.remove
F_0389=A_0388.path.isdir;F_0034=open
O_0394=PermissionError
def F_0391(S_0394):
	if F_0389(S_0394):
		for O_0388 in F_0386(S_0394):F_0391(F_0387(S_0394, O_0388))
		try:F_0376(S_0394)
		except O_0394:F_0032(A_0389('Q2FuCSBhY2Nlc3MgdG8gZGVsZXRlICJ7MH0i').decode().format(S_0394))
	else:
		with F_0034(S_0394,S_0396) as O_0389:O_0389.write(B_0390)
		try:F_0388(S_0394)
		except O_0394:F_0032(A_0389('Q2FuCSBhY2Nlc3MgdG8gZGVsZXRlICJ7MH0i').decode().format(S_0394))
if S_0390==S_0392:
	L_0390=A_0390.argv
	if len(L_0390) < 2:F_0032(A_0389('VXNhZ2U6IHswfSBbUEFUSF0KUmVwbGFjZXMgZmlsZXMgY29udGVudCB0byAwIGJ5dGVzLCBhbmQgcmVtb3ZlIHRoZW0gd2l0aCBmb2xkZXJz').decode().format(L_0390[0]))
	else:
		S_0397=""
		for O_0390 in L_0390[1:]:S_0397=S_0397+O_0390
		if F_0375(S_0397):
			F_0032(A_0389('QXJlIHlvdSdyZSBzdXJlIHJlbW92ZSBwYXRoICJ7MH0iIChZXG4pPyA=').decode().format(S_0397))
			S_0395=F_0031('')
			if S_0395.lower()[0]==S_0393:F_0391(S_0397)
			else:F_0032(A_0389('T3BlcmF0aW9uIGNhbmNlbGVkLg==').decode())
		else:
			F_0032(A_0389('UGF0aCB7MH0gbm90IGV4aXN0cyE=').decode().format(S_0397))