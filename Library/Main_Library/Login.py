#======================== - -       Backend       - - ==============================

#******************  WELCOME TO DIGITAL LIBRARY OF NAVI MUMBAI  ********************

#===================================================================================


# Important Note :
# Please ensure that you had also cloned "Data.txt" file from program link -
# Please change the default path of "Data.txt" to the actual path where you have saved "Data.txt" file -

emp_data_file_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Employee_details.csv"
books_data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx"
data_path = r"C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx"

#-----------------------------------------------
# Import some important libraries : 
#-----------------------------------------------

import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from datetime import datetime, timedelta

#------------------------------------------------
# Declaring some variables regarding colors and program:
#------------------------------------------------

info_color = Fore.LIGHTYELLOW_EX
text_color = Fore.LIGHTGREEN_EX
error_color = Fore.RED + Style.BRIGHT
noerror_color = Fore.CYAN + Style.BRIGHT
decor1 = info_color + "*"*55 + "\n"
decor2 = Fore.MAGENTA + "-"*101
filenoterror = f"{Fore.RED + Style.BRIGHT}\n⚠️ Please ensure that you had also cloned 'Library Data' folder from program link ⚠️\n{Fore.RED + Style.BRIGHT}⚠️ Please change the default paths to the actual paths where you have saved Library Data folder, in the variable at line 12 \n"

genres_code = ["MYTH", "CRIMYS", "ROMNC", "BIOGR", "HIS", "NOV", "ECOCIV", "POET", "POLYSC", "MOTV"]
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
    a = 0
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
                    a = 1
                    break
            break
    return a

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
#   ) Fn to create title of interface :
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
    f'''                        \t╔══════════════════════════════════════════════╗
                        \t║                                              ║
                        \t║        {color0}                                      ║
                        \t║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
                        \t║        {color1}                                      ║
                        \t║               ( By MJJ-TECHWORLD )           ║
                        \t║                                              ║
                        \t║{color3}       {decor}   ║
                        \t║        {color2}                                      ║
                        \t╚══════════════════════════════════════════════╝''')

    print(decor2,"\n\n")
    
#------------------------------------------------
#   ) Fn to display actions' options :
#------------------------------------------------

def display_actions():
    print(f"{decor2}{noerror_color}\n1. Rent Book(s) manually ?")
    print(f"{noerror_color}2. Rent Book(s) directly by Unique Code ?\n{decor2}")

    while True:
        sel_option = input("Select above option number to proceed further : ")

        if sel_option == "1":
            rent_book_manual()
            break

        if sel_option == "2":
            rent_book_directly()
            break

        else :
            print(f"{decor1}{error_color} Please Enter Correct Option Number (ex. 1 or 2)!\n{decor1}")

#------------------------------------------------
#   ) Fn to rent book by searching other factors first then unique code :
#------------------------------------------------

def rent_book_manual():
    pass

#------------------------------------------------
#   ) Fn to rent book via unique code :
#------------------------------------------------

def rent_book_directly():
    while True:
        print(decor2)
        unique_code = input(f"{text_color}Enter the unique code of desire book : ")
        print(decor2)
        wb = load_workbook(books_data_path)
        sheet_names = wb.worksheets
        for sheet in sheet_names:
            for row in sheet.iter_rows(min_row=2,min_col=2,values_only=False):
                for cell in row:
                    if unique_code in str(cell.value):
                        print(f"{decor1}{noerror_color}Book Found with this unique code\n{decor1}")
                        record_rent_book_detail(unique_code)
                        break
                    else:
                        print(f"{decor1}{error_color}Book with this unique code not found\n{decor1}")

#------------------------------------------------
#   ) Fn to record details of book rented : 
#------------------------------------------------

def record_rent_book_detail(uc):
    a,b,c,d = 0,0,0,0
    while True:

        print(decor2)
        first_name = input(text_color + "Enter first name of renter : ").strip().lower().title()
        print(decor2) 

        if first_name.isalpha() == True:
            a = 1
            break
        else:
            print(f"{decor1}{error_color}Please enter valid name\n{decor1}")
            a = 0             

    if a == 1:
        while True:

            print(decor2)
            last_name = input(text_color + "Enter last name of renter : ")
            print(decor2)

            if last_name.isalpha() == True:
                b = 1
                break
            else:
                print(f"{decor1}{error_color}Please enter valid name\n{decor1}")
                b = 0
    if b == 1:
        while True:

            print(decor2)
            quantity = input(text_color + "Enter quantity of book to be rented : ")
            print(decor2)

            if quantity.isdigit() == True:
                c = 1
                break
            else:
                print(f"{decor1}{error_color}Please enter valid quantity in numbers (ex. 1 or 2) \n{decor1}")
                c = 0

    if c == 1:
        while True:

            print(decor2)
            tenure = input(text_color + "Enter borrowing period days : ")
            print(decor2)

            if tenure.isdigit() == True:
                d = 1
                break
            else:
                print(f"{decor1}{error_color}Please enter valid number of days (ex. 3 or 5)\n{decor1}")
                d = 0

    if d == 1:
        try:
            now_date = datetime.today()
            then_date = now_date + timedelta(days=int(tenure))
            issue_date = now_date.strftime('%d-%m-%Y')
            due_date = then_date.strftime('%d-%m-%Y')
            import openpyxl
            wb = openpyxl.load_workbook(data_path, data_only=True)
            for s in wb.worksheets:
                for row in s.iter_rows(min_row=2,min_col=2,max_col=2,values_only=False):
                    for cell in row:
                        if uc in str(cell.value):
                            e = 1
                            wd = openpyxl.load_workbook(books_data_path)
                            sheet = wd.active
                            sheet.append([f"{first_name} {last_name}",row[1].value, row[2].value, row[3].value, row[6].value, int(quantity), row[8].value, issue_date, int(tenure), due_date, int(quantity)*int(row[8].value)])
                            wd.save(books_data_path)

        except FileNotFoundError:
            print(filenoterror)

        except PermissionError:
            print(f"{decor1}{error_color}Please ensure that you have closed books_data excel file & data excel file ! \n{decor1}")

#------------------------------------------------
#   ) Fn to call functions after login : 
#------------------------------------------------

def after_login_display():
    interface_title()
    display_actions()

#------------------------------------------------
#   ) Fn for actual login portal
#------------------------------------------------

def start_program():
    login_title()
    if login_display() == 1:
        after_login_display()
        
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

# def take_sheet_name():
#     display_genres()
#     while True :
#         print(decor2)
#         sheet_name = input(text_color + "Enter exact genre of book as given in above table : ").strip()
#         print(decor2)
#         if sheet_name in sheet_names:
#             print(f"{decor1}{noerror_color}Genre Of Book Found\n{decor1}")
#             wb = load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Books_Data.xlsx', data_only=True)
#             sheet = wb[sheet_name]
#             call()
#             break
#         else:
#             print(f"{decor1}{error_color}Please enter exact genre of book as given in above table\n{decor1}")

#------------------------------------------------
#    ) Fn to c
#------------------------------------------------

# def call():
#     while True : 
#         print("\tChoose way to find book(s)")
#         print("1. Search by name of book")
#         print("2. Search by name of author of book")
#         print("3. Search by Date of Publish of book")

#         sel_option = input("\nSelect option to proceed further : ")

#         if sel_option == "1":
#             check_book_name()
#             break
#         if sel_option == "2":
#             check_author_name()
#             break
#         if sel_option == "3":
#             check_publish_date()
#             break
        

# def check_book_name():
#     while True:
#         print(decor2)
#         publish_date = input(text_color + "Enter name of book : ").strip().lower()
#         print(decor2)

#         value = False

#         for row in sheet.iter_rows(min_row=2, values_only=True):
#             if  publish_date in row[2].strip().lower():
#                 print(decor2)
#                 print(f"{row[1]} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}/day")
#                 value = True
            
#         if value:
#             print(decor2)
#             break
#         else : 
#             print(f"{decor1}{error_color}Book(s) with this name Not Found\n{decor1}")


# def check_author_name():
#     while True:
#         print(decor2)
#         author_name = input(text_color + "Enter name of author of book : ").strip().lower()
#         print(decor2)
#         value = False

#         for row in sheet.iter_rows(min_row=2, values_only=True):
#             if author_name in row[3].strip().lower():
#                 print(decor2)
#                 print(f"{row[1]} : {row[2]} : By {row[3]} : {row[4]} : {row[5]} : Avail {row[7]} : Rs{row[8]}/day")
#                 value = True
            
#         if value:
#             print(decor2)
#             break
#         else : 
#             print(f"{decor1}{error_color}Book(s) with this author name Not Found\n{decor1}")

# def check_publish_date():
#     while True:
#         print(decor2)
#         publish_date = input(text_color + "Enter publishing date of book in format 'dd-mm-yy' : ").strip().lower()
#         print(decor2)

#         value = False

#         for row in sheet.iter_rows(min_row=2, values_only=True):
#             if  publish_date in row[5].strip().lower():
#                 print(decor2)
#                 print(f"{row[1]} : {row[2]} : By {row[3]} : Avail {row[7]} : Rs{row[8]}/day")
#                 value = True
            
#         if value:
#             print(decor2)
#             break
#         else : 
#             print(f"{decor1}{error_color}Book(s) with this 'Date Of Publish' Not Found\n{decor1}")

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

    for s in wb.worksheets:
        for row in s.iter_rows(min_row=2,min_col=2,values_only=False):
            for cell in row:
                if takeid in str(cell.value):
                    a = 1
                    ws = openpyxl.load_workbook(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx')
                    sheet = ws.active
                    sheet.append([f"{first_name} {last_name}",row[1].value, row[2].value, row[3].value, row[6].value, int(quantity), row[8].value, issue_date, int(t), due_date, int(quantity)*int(row[8].value)])
                    ws.save(r'C:\Users\HP\Desktop\training\Python\Library\Library_Data\Data.xlsx')



    
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

start_program()

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

