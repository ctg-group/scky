from core.colors import *
def parse_args(string):
  result = [];tmp0="";pass_spec = False;pass_space = False
  if not " " in string: return [string]
  for c in string:
    if c == " ":
      if pass_space: 
        tmp0+=' '
      else:
        if tmp0!='':
          result.append(tmp0)
          tmp0=''
    elif c == '"':
      if pass_spec:
        pass_spec = False
        tmp0+='"'
      else:
        if pass_space:
          pass_space = False
          result.append(tmp0)
          tmp0=''
        else:pass_space = True
    elif c == '\\':
      if pass_spec: tmp0+='\\'
      else: pass_spec = True
    else: tmp0+=c
  if tmp0!='':result.append(tmp0)
  return result

def question_yn(question):
  inp = input(question+' (y\\n): ').lower()
  if inp[0]=='y': return True
  elif inp[0]=='n': return False
  else:
    print(f'[{R}-{N}] Please, retry!')
    question_yn(question)

def clear():
  import sys, os
  if sys.platform.lower().startswith('win'):
    os.system('cls')
  else:
    os.system('clear')