from colorama import *
class colormate:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   BAWHITE = '\033[47m'
   BLACK = '\033[30m'
   WHITE = '\033[37m'
   REVERSE = '\033[2m'
   ORIGINALCOLOR = '\033[0;0m'
   BABLACK = '\033['
   BARED = '\033[41m'
   BAGREEN = '\033[42m'
   BAYELLOW = '\033[43m'
   BABLUE = '\033[44m'
   BAPURPLE = '\033[45m'
   BACYAN = '\033[46m'
   HELP = print( f'PURPLE CYAN DARKCYAN BLUE GREEN YELLOW RED BOLD UNDERLINE END BLACK WHITE REVERSE ORIGINAL COLOR BAWHITE BABLACK BARED BAGREEN BAYELLOW BABLUE BAPURPLE BACYAN')
try:
    from colorama import init
    init(autoreset=True)
    print(colormate.GREEN + f'Você está pronto')

except ModuleNotFoundError:
    print(f'Instale o modulo necessario chamado colorama')
