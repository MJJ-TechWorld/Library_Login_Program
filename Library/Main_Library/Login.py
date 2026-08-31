#======================== - -       Backend       - - ==============================

#******************  WELCOME TO DIGITAL LIBRARY OF NAVI MUMBAI  ********************

#===================================================================================


# Important Note :
# Please ensure that you had also cloned "Data.txt" file from program link -
# Please change the default path of "Data.txt" to the actual path where you have saved "Data.txt" file -

emp_data_file_path = r"C:\Users\HP\Desktop\training\Python\Library\Employee_details.csv"

#-----------------------------------------------
# Import some important libraries : 
#-----------------------------------------------

import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from datetime import datetime, timedelta
#------------------------------------------------
# Declaring some variables regarding colors :
#------------------------------------------------

info_color = Fore.LIGHTYELLOW_EX
text_color = Fore.LIGHTGREEN_EX
error_color = Fore.RED + Style.BRIGHT
noerror_color = Fore.CYAN + Style.BRIGHT
decor1 = info_color + "*"*50 + "\n"
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

#------------------------------------------------
#   ) Fn for displaying genres in excel in proper format :
#------------------------------------------------

def display_genres():
    try : 
        global sheet_names
        print(decor2, "\n")

        wb = load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx')
        sheet_names = wb.sheetnames
        for i in sheet_names:
            if sheet_names.index(i) % 2 == 0:
                print(f"   {info_color}{i:<50}|", end = "")
            else:
                print(f"{info_color}{i:>50}")

        print("\n", decor2)

    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + "\n⚠️ Please ensure that you had also cloned 'Library Data' folder from program link ⚠️")
        print(Fore.RED + Style.BRIGHT + "⚠️ Please change the default paths to the actual paths where you have saved Library Data folder, in the variable at line 12 \n")

#------------------------------------------------
#    ) Fn to go to the desire sheet :
#------------------------------------------------

def take_sheet_name():
    display_genres()
    global sheet
    while True :
        print(decor2)
        sheet_name = input(text_color + "Enter exact genre of book as given in above table : ").strip()
        print(decor2)
        if sheet_name in sheet_names:
            print(f"{decor1}{noerror_color}Genre Of Book Found\n{decor1}")
            wb = load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx', data_only=True)
            sheet = wb[sheet_name]
            call()
            break
        else:
            print(f"{decor1}{error_color}Please enter exact genre of book as given in above table\n{decor1}")

#------------------------------------------------
#    ) Fn to c
#------------------------------------------------

def call():
    while True : 
        print("\tChoose way to find book(s)")
        print("1. Search by name of book")
        print("2. Search by name of author of book")
        print("3. Search by Date of Publish of book")

        sel_option = input("\nSelect option to proceed further : ")

        if sel_option == "1":
            check_book_name()
            break
        if sel_option == "2":
            check_author_name()
            break
        if sel_option == "3":
            check_publish_date()
            break
        

def check_book_name():
    while True:
        print(decor2)
        publish_date = input(text_color + "Enter name of book : ").strip().lower()
        print(decor2)

        value = False

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if  publish_date in row[2].strip().lower():
                print(decor2)
                print(f"{row[1]} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}/day")
                value = True
            
        if value:
            print(decor2)
            break
        else : 
            print(f"{decor1}{error_color}Book(s) with this name Not Found\n{decor1}")


def check_author_name():
    while True:
        print(decor2)
        author_name = input(text_color + "Enter name of author of book : ").strip().lower()
        print(decor2)
        value = False

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if author_name in row[3].strip().lower():
                print(decor2)
                print(f"{row[1]} : {row[2]} : By {row[3]} : {row[4]} : {row[5]} : Avail {row[7]} : Rs{row[8]}/day")
                value = True
            
        if value:
            print(decor2)
            break
        else : 
            print(f"{decor1}{error_color}Book(s) with this author name Not Found\n{decor1}")

def check_publish_date():
    while True:
        print(decor2)
        publish_date = input(text_color + "Enter publishing date of book in format 'dd-mm-yy' : ").strip().lower()
        print(decor2)

        value = False

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if  publish_date in row[5].strip().lower():
                print(decor2)
                print(f"{row[1]} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}/day")
                value = True
            
        if value:
            print(decor2)
            break
        else : 
            print(f"{decor1}{error_color}Book(s) with this 'Date Of Publish' Not Found\n{decor1}")

def id():
    first_name = input("Enter first name : ")
    last_name = input("Enter last name : ")
    takeid = input("Enter Unique Code : ")
    quantity = input("Enter quantity of books : ")
    t = input("Enter tenure : ")
    from datetime import timedelta, datetime
    now_date = datetime.today()
    then_date = now_date + timedelta(days=int(t))
    issue_date = now_date.strftime('%d-%m-%Y')
    due_date = then_date.strftime('%d-%m-%Y')
    import openpyxl
    wb = openpyxl.load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx', data_only=True)
    a = 0

    for i in wb.worksheets:
        for row in i.iter_rows(values_only=False):
            for cell in row:
                if takeid in str(cell.value):
                    a = 1
                    ws = openpyxl.load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx')
                    sheet = ws.active
                    sheet.append([f"{first_name} {last_name}",row[1].value, row[2].value, row[3].value, row[6].value, int(quantity), row[8].value, issue_date, int(t), due_date, int(quantity)*int(row[8].value)])
                    ws.save(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx')
id()


    
    # wb = load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx')
    # sheet = wb.active
    # sheet["A2"] = f"{first_name} {last_name}"
    # sheet["B2"] = d[1]
    # sheet["C2"] = d[2]
    # sheet["D2"] = d[3]
    # sheet["E2"] = d[6]
    # sheet["F2"] = q
    # sheet["G2"] = int(d[6])*int(q)
    # wb.save(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx')

#==================================================================================================
# Calling functions : 

#login_portal()
# take_sheet_name()
# first_name = input("Enter first name : ")
# last_name = input("Enter last name : ")
# code = input("Enter unique code : ")
# q = input("Enter quantity of books : ")
# detail = []
# from openpyxl import load_workbook
# wa = load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx')
# sheet = wa["Mythology"]
# for row in sheet.iter_rows(min_row=2,values_only=True):
#     if row[1] == code:
#         detail.append(row)
# d = list(detail[0])
# wa.save(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx')    

# wb = load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx')
# sheet = wb.active
# sheet["A2"] = f"{first_name} {last_name}"
# sheet["B2"] = d[1]
# sheet["C2"] = d[2]
# sheet["D2"] = d[3]
# sheet["E2"] = d[6]
# sheet["F2"] = q
# sheet["G2"] = int(d[6])*int(q)
# wb.save(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx')