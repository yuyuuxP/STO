import os
import sys
import utility
from controllers.user_controller import create_user

if __name__ == "__main__":
    o = os.name
    match os.name:
        case "nt" : os.system("cls")

utility.greeting_prompt()
while True:
    chooseMenuAcc = utility.account_menu()
    os.system("cls")
    match chooseMenuAcc:
        case "1":
            username,password = utility.create_account_prompt()
            create_user(username,password)
        case "2":
            utility.log_account_prompt()
            break
        case "3": 
            utility.exit_prompt()
            sys.exit(0)
        case _:
            print("Invalid")
            continue