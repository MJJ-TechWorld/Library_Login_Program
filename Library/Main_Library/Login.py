#======================== - -       Backend       - - ==============================

#******************  WELCOME TO DIGITAL LIBRARY OF NAVI MUMBAI  ********************

#===================================================================================


# Important Note :
# Please ensure that you had also cloned "Data.txt" file from program link -
# Please change the default path of "Data.txt" to the actual path where you have saved "Data.txt" file -

emp_data_file_path = r"C:\Users\HP\Desktop\training\Python\Employee_details.csv"

#-----------------------------------------------
# Import some important libraries : 
#-----------------------------------------------

import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)

#------------------------------------------------
# Declaring some variables regarding colors :
#------------------------------------------------

info_color = Fore.LIGHTYELLOW_EX
text_color = Fore.LIGHTGREEN_EX
error_color = Fore.RED + Style.BRIGHT
noerror_color = Fore.CYAN + Style.BRIGHT
decor1 = info_color + "*"*25 + "\n"
decor2 = Fore.MAGENTA + "-"*101

#------------------------------------------------
#  1) Fn of displaying title :
#------------------------------------------------

def login_title():
    a = Back.LIGHTCYAN_EX + "     "
    r = Fore.GREEN + Style.BRIGHT
    b = Fore.BLUE + Style.BRIGHT + Back.LIGHTYELLOW_EX
    re = Fore.RED  + Back.LIGHTMAGENTA_EX
    s = " "*101
    d,t1,T1,t2,t3,t4 = "*"*50,"="*91," "*85,"💻     PUBLIC LIBRARY     💻","OF","🗺️      NAVI MUMBAI       🗺️"
    t5 = "( By MJJ-TECHWORLD )"

    print("\n\n")
    print(Back.LIGHTCYAN_EX + s)
    print(a,r + t1,a, sep = "")
    print(a,r + t1,a, sep = "")
    print(a,r + "|| ",r + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + f"{t2:^83}",r + " ||",a, sep = "")
    print(a,r + "|| ",b + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + f"{t3:^85}",r + " ||",a, sep = "")
    print(a,r + "|| ",b + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + f"{t4:^87}",r + " ||",a, sep = "")
    print(a,r + "|| ",b + T1,r + " ||",a, sep = "")
    print(a,r + "|| ",b + f"{d:^85}",r + " ||",a, sep = "")
    print(a,r + "|| ",re + f"{t5:^85}",r + " ||",a, sep = "")
    print(a,r + "|| ",r + T1,r + " ||",a, sep = "")
    print(a,r + t1,a, sep = "")
    print(a,r + t1,a, sep = "")
    print(Back.LIGHTCYAN_EX + s, "\n\n")

#------------------------------------------------
#  2) Fn for displaying login options :
#------------------------------------------------

def login_display():
    global username, password
    login_title = "--- LOGIN PORTAL ---"
    print(info_color + "="*100)
    print(Fore.CYAN + f"\n{login_title:^101}\n")
    print(info_color + "*"*100 + "\n\n")

    while True:
        print(decor2)
        username = input(text_color + "Enter Your Username : ").strip()
        print(decor2)

        if check_username(username) == "yes": 

            while True:
                print(decor2)
                password = input(text_color + "Enter Your Password : ").strip()
                print(decor2)

                if check_password(username,password) == "yes":
                    interface()
                    break
            break

#------------------------------------------------
#  3) Fn for checking username : 
#------------------------------------------------

def check_username(u):
    try:
        with open(emp_data_file_path, "r") as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                if (row and row[1] == u):
                    print(f"\n{decor1}{noerror_color}   Username Found\n{decor1}")
                    return "yes"
                
            print(f"\n{decor1}{error_color}  ⚠️  Invalid Username ⚠️\n{decor1}")
        
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + "\n⚠️ Please ensure that you had also cloned 'Library Data' folder from program link ⚠️")
        print(Fore.RED + Style.BRIGHT + "⚠️ Please change the default paths to the actual paths where you have saved Library Data folder, in the variable at line 12 \n")

#------------------------------------------------
#  4) Fn to check password :
#------------------------------------------------

def check_password(u,p): 
    try: 
        with open(emp_data_file_path, "r") as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                if (row and len(row)>1 and row[1] == u  and row[2] == p):
                    print(f"\n{decor1}{noerror_color}  Logged in successfully!\n{decor1}")
                    return "yes"

            print(f"\n{decor1}{error_color}  ⚠️   Wrong Password ⚠️\n{decor1}")
        
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + "\n⚠️ Please ensure that you had also cloned 'Library Data' folder from program link ⚠️")
        print(Fore.RED + Style.BRIGHT + "⚠️ Please change the default paths to the actual paths where you have saved Library Data folder, in the variable at line 12 \n")

#------------------------------------------------
#  5) Fn to create title of interface :
#------------------------------------------------

def interface_title():
    print(decor2)
    print(decor2, "\n")
    color0 = Fore.YELLOW
    color1 = Fore.GREEN
    color2 = Fore.CYAN
    color3 = Fore.MAGENTA
    decor = "*"*36
    print(Fore.CYAN + 
    f'''                        ╔══════════════════════════════════════════════╗
                        ║                                              ║
                        ║        {color0}                                      ║
                        ║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
                        ║        {color1}                                      ║
                        ║               ( By MJJ-TECHWORLD )           ║
                        ║                                              ║
                        ║{color3}       {decor}   ║
                        ║        {color2}                                      ║
                        ╚══════════════════════════════════════════════╝''')

    print(decor2,"\n\n")
#------------------------------------------------
#   ) Fn to display actions' options :
#------------------------------------------------

def actions():
    print("\n\tNew Buyer ?\n")
    print("1. Buy book(s) ")

    print()

#------------------------------------------------
#   ) Fn to call actual interface :
#------------------------------------------------

def interface():
    interface_title()

#------------------------------------------------
#   ) Fn for actual login portal
#------------------------------------------------

def login_portal():
    login_title()
    login_display()

#==================================================================================================
# Calling functions : 
login_portal()

