from colorama import Fore, init
import time
import sys

init(autoreset=True)

def welcomeGabriel():
    titulo = """
.___  __        .___   _____ ___.          .__  .__   
|   _/  |_ _____|   | /  _  \\_ |__   ____ |  | |  |  
|   \   __/  ___|   |/  /_\  \| __ \_/ __ \|  | |  |  
|   ||  | \___ \|   /    |    | \_\ \  ___/|  |_|  |__
|___||__|/____  |___\____|__  |___  /\___  |____|____/
              \/            \/    \/     \/      

           ItsIAbell IA Agent v1.0.0
"""

    print("\n")
    for i in range(len(titulo) + 1):
        sys.stdout.write("\r" + Fore.YELLOW + titulo[:i])
        sys.stdout.flush()
        time.sleep(0.001) 

    print(Fore.CYAN + "\nHola Gabriel Soy ItsIAbell soy tu primera IA con neuronas 4B Primer\n")
 