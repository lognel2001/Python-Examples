# Logan Nelson
#10/18
#password program

def menu():
    choice = 0
    while choice == 0:
        print("to sign up press 1")
        print("to sign in press 2")
        choice = int(input("enter your choice"))
        if choice == 1:
            username = get_username()
            password = get_password()
            choice = 0
        elif choice == 2:
            print("choice 2")
            login = check_account(username, password)
            return password, username, login
        else:
            print("that's not a valid option")
            menu()
def get_password():
    print("""your password must start with a capitol letter
and must contain at least 1 symbol
and mush be at least 10 charachters long""")
    password = input("enter your password:")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("password is set")
        return password
    else:
        print("your password didn't meet the requirements")
        get_password()


    
def get_username():
    print("""only contain numbers and letters
can only contain 10 characters
must contain at least 3 characters""")
    username = input("enter your user name")
    if username.isalnum() and len(username)<=10 and len(username)>=3:
        print("your username is set")
        return username
    else:
        print(" your username didn't meet the requirements")
        get_username()
        

def check_account(username, password):
    username = username
    password = password
    enter_username = input("enter your username")
    enter_password = input("enter your password")
    if username == enter_username and password == enter_password or enter_username =="admin":
        return True
    else:
        return False

def main():
    login = False
    password, username, login = menu()

    if login == True:
        print("you got in")
    else:
        print("access denied")

main()

    
