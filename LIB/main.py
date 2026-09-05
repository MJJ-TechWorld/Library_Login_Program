#----------------    BACKEND    -----------------

#------------------------------------------------
# IMPORTANTS IMPORTS FOR THIS PROGRAM
#------------------------------------------------

import openpyxl
from colorama import init, Fore, Back, Style
init(autoreset=True)
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from rich import console
from datetime import datetime, timedelta
from pyfiglet import figlet_format


import csv
import random
import time
import uuid
import os

from getpass import getpass
from datetime import datetime, timedelta
from pyfiglet import figlet_format

from rich.console import Console
from rich.table import Table
from rich.progress import track

#------------------------------------------------
# ASSIGNING IMP PATHS TO THE VARIABLES
#------------------------------------------------

books_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\books_data.xlsx"
users_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\users_data.xlsx"
empls_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\empls_data.csv"
credt_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\credentials.txt"

#------------------------------------------------
# PROGRAM START FROM HERE :
#------------------------------------------------

# DEFINING IMP FUNCTIONS USED IN THIS PROGRAM ---

def display_login_title():
    pass
if __name__ == "__main__":
    while True:
        username = input("Enter Your Username : ")
