import os
import platform
from setup import colors
from setup.colors import r,g,y,c

logo = f"""


       _
  ___| |__  _ __ ___  _ __ ___   ___
 / __| '_ \| '__/ _ \| '_ ` _ \ / _ \
| (__| | | | | | (_) | | | | | |  __/
 \___|_| |_|_|  \___/|_| |_| |_|\___|

 ____                                     _       _             _
|  _ \ __ _ ___ _____      _____  _ __ __| |  ___| |_ ___  __ _| | ___ _ __
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | / __| __/ _ \/ _` | |/ _ \ '__|
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| | \__ \ ||  __/ (_| | |  __/ |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |___/\__\___|\__,_|_|\___|_|




                             {c + "coded By: hacker_6_2_9_1"+y +" "}             
                                                                                                                   
"""
c = colors
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")

def banner():
    print(c.ran + logo)
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @qadirahmad ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @qadirahmad6291 ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/hacker629 ", "- " * 3+c.ran + "|")
    print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)


def banner2():
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @qadirahmad ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram@qadirahmad6291", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github:  https://github.com/hacker6291  ", "- " * 3+c.ran + "|")
    print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")
