
import sys
import colorama

if sys.platform.lower().startswith('win'):
    colorama.init()

R = colorama.Fore.RED
G = colorama.Fore.GREEN
B = colorama.Fore.BLUE
Y = colorama.Fore.YELLOW
C = colorama.Fore.CYAN
N = colorama.Fore.RESET