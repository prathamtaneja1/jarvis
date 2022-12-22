import os

def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()

def play():
# Driver's code
# Printing CWD before
    current_path()
 
# Changing the CWD
    os.chdir('D:\\Coding\\Python\\Games\\Shooting_game')
 
# Printing CWD after
    current_path()
    os.system("D:\\Coding\\Python\\Games\\Shooting_game\\Computer.exe")
