#======================== - -       Backend       - - ==============================

#******************  WELCOME TO DIGITAL LIBRARY OF NAVI MUMBAI  ********************

#===================================================================================

# Important Note :
# Please ensure that you had also cloned "Data.txt" file from program link -
# Please change the default path of "Data.txt" to the actual path where you have saved "Data.txt" file -

data_file_path = r"C:\Users\HP\Desktop\training\Python\library\Data.txt"


#===================================================================================
#Defining all required function :-
#---------------------------------

# 1) Fn for creating first name of user :
def create_first_name():
    print("-"*100)
    while True:
        global new_first_name 
        new_first_name = input(f"Enter your First Name : ").strip().lower().title()
        exit_login(new_first_name) # To exit login session
        exit_program(new_first_name) # To exit program
        # It will ask user until correct name doesn't entered
        if (new_first_name.isalpha()==False):
            print("\n⚠️ Please Enter Name properly ⚠️\n")
        else:
            print("-"*100)
            break
        
#------------------------------------------------------------------------------
# 2) Fn for creating last name of user :  

def create_last_name():
    while True:
        global new_last_name
        new_last_name = input(f"Enter your Last name : ").strip().lower().title()
        exit_login(new_last_name) # To exit login session
        exit_program(new_last_name) # To exit program
        # It will ask user until correct name doesn't entered
        if (new_last_name.isalpha()==False):
            print("\n⚠️ Please Enter Name properly ⚠️\n")
        else:
            print("-"*100)
            break

#------------------------------------------------------------------------------
# 3) Fn for creating phone number of user :

def create_phone_number():
    while True:
        global new_mobile_no 
        new_mobile_no = input("Enter your Phone Number : ").strip()
        exit_login(new_mobile_no) # To exit login session
        exit_program(new_mobile_no) #To exit program
        if ( new_mobile_no.isdigit() == False ) or ( len(new_mobile_no) != 10 ) :
            print("\n⚠️ Please enter Mobile Number properly ⚠️\n")
        else:
            print("-"*100)
            break

#------------------------------------------------------------------------------
# 4) Fn for creating Username:
# Format : (MyLib) + (3 char of first name) + (3 char of last name) + (4 digit of phone no.)

def create_new_username():
    global new_username
    new_username = "MyLib" + new_first_name.lower()[:3] + new_last_name.lower()[:3] + new_mobile_no[:4]

#------------------------------------------------------------------------------
# 5) Fn for creating Password:

def create_password():
    global new_pass
    print("\nPassword should be of 8 characters only")
    while True:
        new_pass = input("Create New Password : ")
        exit_login(new_pass) # To exit login session
        exit_program(new_pass) # To exit program
        if (len(new_pass) == 8):
            print("Created password successfully !")
            print("-"*100)
            break
        else:
            print("\n⚠️ Password should contain 8 characters only ⚠️\n")

#------------------------------------------------------------------------------
# 6) Fn for creating Security Pin:

def create_pin():
    global new_pin
    print("\nSecurity Pin should contain 5 digits only")
    while True:
        try:
            new_pin = input("Create Security Pin (only numbers) : ")
            exit_login(new_pin) # To exit program
            exit_program(new_pass)
            if (len(str(new_pin)) == 5):
                print("Created Security pin successfully!")
                print("-"*100)
                break
            else:
                print("\n⚠️ Please enter valid security pin containing 5 digits\n" \
                "Starting digit should not 0\n") 
        except ValueError:
            print("\n⚠️ Security pin should contain only numbers (0-9)\n" \
            "Starting digit should not 0\n")

#------------------------------------------------------------------------------
# 7) Fn for saving data of new user in "Data.txt"
# Format : Username - Password - Pin - First name Last name - phone number \n

def add_username_password_pin_name_phone_no():
    try:
        with open(data_file_path, "r") as file:
            datalist = file.readlines()
            for i in range(len(datalist)-1, -1, -1):
                if "=" in datalist[i] and "DIGITAL" not in datalist[i]:
                    break
            datalist.insert(i-1, f"| {new_username} | {new_pass} | {new_pin} | {new_first_name} {new_last_name} | {new_mobile_no} |\n")
            open(data_file_path,"w").writelines(datalist)
    
    except FileNotFoundError:
        print("\n⚠️ Please ensure that you had also cloned 'Data.txt' file from program link ⚠️")
        print("⚠️ Please change the default path to the actual path where you have saved Data.txt' file, in the variable at line 11 \n")

#------------------------------------------------------------------------------
# 8) Fn for checking username directly
def check_username(u):
    try:
        with open(data_file_path, "r") as file:
            data = file.read()
            if (u in data and len(u) == 15):
                a = "yes"
                print("Username Found")
            else:
                a = "no"
                print("⚠️ Invalid Username ⚠️\n")
            return a
        
    except FileNotFoundError:
        print("\n⚠️ Please ensure that you had also cloned 'Data.txt' file from program link ⚠️")
        print("⚠️ Please change the default path to the actual path where you have saved Data.txt' file, in the variable at line 11 \n")

#------------------------------------------------------------------------------
# 9) Fn for checking password :
# How it works ?
# a) It will take username & password as parameters 
# b) It will first find username (of 15 char) and then moves pointer by 18
# c) Here original password will be checked by slicing and match it with user's password
 
def check_password(u,p): 
    try: 
        with open(data_file_path, "r") as file:
            data = file.read()
            t = data.find(u) + 18
            n = data[t:t+8]
            if n == p:
                a = "yes"
                print("Logged in successfully!")
            else:
                a = "no"
                print(" ⚠️ Wrong Password")
            return a
        
    except FileNotFoundError:
        print("\n⚠️ Please ensure that you had also cloned 'Data.txt' file from program link ⚠️")
        print("⚠️ Please change the default path to the actual path where you have saved Data.txt' file, in the variable at line 11 \n")


#------------------------------------------------------------------------------
# 10) Fn for checking security pin:
# How it works ?
# It will works same as for checking password only here pointer shifts by 29

def check_pin(u,p):
    try:
        with open(data_file_path, "r") as file:
            data = file.read()
            t = int(data.find(u) + 29)
            n = data[t:t+5]
            if n == p:
                a = "yes"
                print("Security Pin is correct")
            else:
                a = "no"
                print("\n⚠️ Wrong Security Pin\n")
            return a
            
    except FileNotFoundError:
        print("\n⚠️ Please ensure that you had also cloned 'Data.txt' file from program link ⚠️")
        print("⚠️ Please change the default path to the actual path where you have saved Data.txt' file, in the variable at line 11 \n")

#------------------------------------------------------------------------------
# 11) Fn for changing Password :

def change_password(u): 
    while True:
        np = input("Enter your New Password : ")
        exit_program(np) # exit the program
        if ( len(np) != 8 ):
            print("\nPassword should contain only 8 characters")
        else:
            while True:
                confirm_np = input("Confirm Password : ")
                exit_program(confirm_np) # exit the program
                if (confirm_np != np):
                    print("\nPlease Enter Exact Password as before : ")
                else:
                    try : 
                        print("Your Password has been changed successfully!\n")    
                        with open(data_file_path) as file:
                            datalist = file.readlines()
                        with open(data_file_path, "w") as file:
                            for i in datalist:
                                if u in i:
                                    parts = i.strip().split(" | ")
                                    parts[1] = confirm_np
                                    file.write(" | ".join(parts) + "\n")
                                else:
                                    file.write(i)
                        login()
                        break
                    except FileNotFoundError:
                        print("\n⚠️ Please ensure that you had also cloned 'Data.txt' file from program link ⚠️")
                        print("⚠️ Please change the default path to the actual path where you have saved Data.txt' file, in the variable at line 11 \n")
            break

#------------------------------------------------------------------------------
# 12) Fn for deleting user's account details :

def delete_account(u):
        print(f"⚠️ Account with Username : {u} has been blocked due to security conern ⚠️")
        try:
            with open(data_file_path, "r") as file:
                data = file.read()
                search = f"| {u} "
                point = data.find(search)
                startpoint = data.rfind("\n", 0, point) + 1
                endpoint = data.find("\n", point) +1
                userdetail = data[:startpoint] + data[endpoint:]

            with open(data_file_path, "w") as file:
                file.write(userdetail)
        except FileNotFoundError:
            print("\n⚠️ Please ensure that you had also cloned 'Data.txt' file from program link ⚠️")
            print("⚠️ Please change the default path to the actual path where you have saved Data.txt' file, in the variable at line 11 \n")

#------------------------------------------------------------------------------
# 13) Fn for Forgot Password Option for Users :

def forgot_password():
    print("\n", "-"*100,"\t\t\t\t\tForgot Password\t\t\t\t\t\t\t","-"*100,"", sep ="\n")
    a = "no"
    while True:
        rough_old_username = input("Enter your username : MyLib")
        exit_program(rough_old_username) # exit the program
        old_username = "MyLib" + rough_old_username

        if (check_username(old_username) == "no"):
            a = "no"
            pass    
        else:       
            for i in [3,2,1 ]:
                old_pin = input("Enter your security pin : ")

                if ( check_pin(old_username,old_pin) == "yes"):
                    change_password(old_username)
                    a = "yes"
                    break
                else:
                    if i == 1:
                        delete_account(old_username)
                        a = "no"
                        break
                    else:
                        print(f" ⚠️ You have only {i-1} attempts left for entering security pin ⚠️")
            break
    return a

#------------------------------------------------------------------------------
# 14) Fn for users to try entering password again for 3 times:

def try_password_again(u):
    for attempts_left in [3,2,1]:
        print(f"\n⚠️ You have {attempts_left} attempts left ! ⚠️")
        user_password = input("Enter your Password : ")
        result = check_password(u,user_password)
        exit_login(result) # exit login session
        exit_program(result) # exit the program
        if (result == "yes"):
            interface()
            break
        if (attempts_left == 1 and result == "no"):
            forgot_password()
            break

#------------------------------------------------------------------------------
# 15) Fn giving option to User if entered wrong password :

def password_lock(u):
    a = "no"
    while True:
            try :
                print("-"*100)
                print("What you want to do now ?")
                print("\t1. Try to enter password again (3 attempts then forgot password) ?")
                print("\t2. Forgot Password?")
                sel_option = (input("Enter option number to proceed respective action : "))
                exit_login(sel_option) # exit login session
                exit_program(sel_option) # exit the program
                if (sel_option == "1"):
                    result = try_password_again(u)
                    if (result == "yes"):
                        a = "yes"
                    else:
                        a = "no"
                    break
                elif (sel_option == "2"):
                    result = forgot_password()
                    if (result == "yes"):
                        a = "yes"
                    else:
                        a = "no"
                    break
                else:
                    print("Please Enter Option Number only (ex. 1)")
                    continue

            except ValueError:
                print("Please Enter Option Number only (ex. 1)")
                continue
    return a

#------------------------------------------------------------------------------
# 16) Fn for those users who have username & password : 

def already_login():
    print("-"*100,"\n")
    global old_username
    while True:
        input_old_username = input("Enter your Username : MyLib")
        exit_login(input_old_username) # exit login session
        exit_program(input_old_username) # exit the program
        old_username = "MyLib" + input_old_username
        if (check_username(old_username)== "no"):
            pass
        else:
            old_password = input("Enter your Password : ")
            exit_login(old_password) # exit login session
            exit_program(old_password) # exit the program
            result =  check_password(old_username,old_password)
            if (result == "yes"):
                interface()
                break
            elif ( result == "no"):
                password_lock(old_username)
                break
            else:
                print("Something went wrong")
                break

#------------------------------------------------------------------------------
#              Overall Flow whenever user enters wrong password:
#
# wp = wrong password | cp = correct password | o1 = option1 | 
# o2 = option2 | csp = correct security pin | wsp = wrong security pin
#   
# login (o1) 👉 already_login (wp)👉 password_lock (o1)👉 try_password_again
#                   (cp)                    (o2)               (wp)
#                    👇                      👇                 👇
#                 interface                  ---forgot_password---
#                                              (wsp)       (csp)
#                                                👇          👇
#                                              delete      change
#                                             acccount    password 👉 login          
#==============================================================================           
#------------------------------------------------------------------------------
# 17) Fn for collecting details of New Users :

def new_user():
    title1 = " Welcome New User  "
    print(f"\n{title1:*^100}\n")
    create_first_name()
    create_last_name()
    create_phone_number()
    create_new_username()
    create_password()
    create_pin()
    add_username_password_pin_name_phone_no()
    print("="*100)
    print("\nAccount Created Successfully !\n\n")
    title2 = "New Account Details"
    print("-"*44)
    print(f"|{title2:^42}|")
    print("="*44)
    print(f"| Your First Name    :{new_first_name :>20} |")
    print(f"| Your Last Name     :{new_last_name  :>20} |")
    print(f"| Your Username      :{new_username   :>20} |")
    print(f"| Your Password      :{new_pass       :>20} |")
    print(f"| Your Security Pin  :{new_pin        :>20} |")
    print("-"*44, "\n\n")
    login()

#------------------------------------------------------------------------------
# 18) Fn for login interface welcome:

def welcome_user():
    lib_name = " - DIGITAL LIBRARY OF NAVI MUMBAI - "
    wel = " WELCOME USER "
    print("="*100)
    print(f"{lib_name:*^100}")
    print("="*100, "\n\n")
    print(F"{wel:-^100}")

#------------------------------------------------------------------------------
# 19) Fn of Important Instruction :

def imp_instruction1():
    print("\n\n✯ Important Instructions ✯")
    print("-"*26,"\n")
    print("☞ Type 'exit' and press key 'enter' : Whenever you \n  want to exit the login session (except forgot password)")
    print("☞ Type 'exit' and press key 'e' : Whenever you want\n  to exit the program!")

#-----------------------------------------------------------------------------
# 20) Fn for exits :

def exit_login(el):
    exit_program(el)
    el = el.strip().lower()
    if (el == "exit"):
        print("\nLogin Session exited!\n")
        login()
    else:
        pass


def exit_program(ep):
    ep = ep.strip().lower()
    if (ep == "e"):
        print("\nProgram exited!\n")
        exit()
    else:
        pass

#------------------------------------------------------------------------------
# 20) Fn for Login options for Users : 

def login():
    dummy_var = " LOGIN PORTAL "
    print("="*100,"", f"{dummy_var:^100}", "", sep = "\n")

    print("-"*100,"\n")
    print("1.New User? Create account here.")
    print("2.Already signed in? Sign up here.\n")
    while True:
        try:
            sel_option = input("Enter option number to proceed respective action : ")
            exit_login(sel_option) # exit login session
            exit_program(sel_option) # exit the program
            if (sel_option == "1"):
                new_user()
                break
            if (sel_option == "2"):
                already_login()
                break
            else:
                print("Enter only one option (1 or 2)")
        except ValueError as a:
            print("Please Enter Option Number only (ex. 1)")

#------------------------------------------------------------------------------
# 20) Fn of actual library:

def interface():
    print("\n\n\t\t\tWelcome Digital Library Of Navi Mumbai\t\t")
    print("="*100)

#===================================================================================
welcome_user()
imp_instruction1()
login()

