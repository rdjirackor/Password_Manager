def create_user():
    user_name = input("What is your Name? :")
    user_email = input("What is your email address?, this will\nbe used in case you forget your password :")
    user_password = input("Create a master password, preferable a passphrase :")
    return {"User": user_name, "Email": user_email, "Central_pass": user_password}


def confirm_password(password):
    confirmed_one = input("Re-Enter the password, you forgetful geezer :")
    while confirmed_one != password:
        print("The two passwords don't match, so we'll start again")
        user = create_user()
        password = user["Central_pass"]
        confirmed_one = input("Re-Enter the password, you forgetful geezer :")
        if confirmed_one == password:
           return confirmed_one
            
        
    #print(f"Your accepted password is {confirmed_one}")


user = create_user()
initially_given_password = user["Central_pass"]
confirm_password(initially_given_password)
