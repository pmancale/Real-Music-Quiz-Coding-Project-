import csv

login_status = 0

username = ""
password = ""

username_reg = ""
password_reg = ""

def ask_up():
    global username
    global password
    username = input("Username?")
    password = input("Password?")

def ask_reg():
    global username_reg
    global password_reg
    username_reg = input("Username?")
    password_reg = input("Password?")


def login():

    ask_up()

    global login_status
    global username
    global password

    with open("login.csv", "r" ) as file:
        content_logins = csv.reader(file, delimiter=",")
        for row in content_logins:
            if row == [username,password]:
                print("Login successful!")
                login_status = True 
    
            else:
                print("Login attempt failed!")
                login_status = False
                print(username, password)
        



def register():
    
    ask_reg()

    global username_reg
    global password_reg

    with open("login.csv", "a", newline='') as file:
        content_logins = csv.writer(file, delimiter=",")
        content_logins.writerow([username_reg, password_reg])
        print("Registration successful!")
        print("You can now login with your new account.")

        print("Would you like to login now? (yes/no)")
        login_now = input()
        if login_now.lower() == "yes":
            main()
        else:
            print("You can login later by running the program again.")




def main():
    print("Would you like to login or register a new account? (login/register)")
    login_or_register = str(input())
    if login_or_register == "login":
        login()
    elif login_or_register == "register":
        register()



if __name__ == "__main__":
    main()
    
 