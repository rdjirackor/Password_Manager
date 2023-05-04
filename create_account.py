def create_user():
    user_name=str(input("What is your Name? :",))
    user_email=str(input("What is your email address?, this will \n be used in case you forget your password :",))
    user_password=str(input("Create a master password, preferable a passphrase :",))
    return {"User":user_name, "Email":user_email,"Central_pass":user_password}
#Te variabl below is assigned a weird meaningless name, but it means im trying to access the password the user made before, so well keep up
pletti=create_user()
initially_given_password=pletti["Central_pass"]


def confirm_password(password):
    confirmed_one=str(input("Re-Enter the password, you forgetful geezer :",))
    #if confirmed_one==password:
    #    print("Well, look at you being all alert!")
     #   return confirmed_one
    #else:
     #   print("The two password dont match, try again")
     #  create_user()
    while confirmed_one!=password:
       print("The two password dont match, so we'll start again")
       create_user()
       if confirmed_one==password:
           break
       return confirmed_one
final_password=confirm_password(pletti["Central_pass"])
print(f"Your accepted password is {final_password}")