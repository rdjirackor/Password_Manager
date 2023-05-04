import hashlib
import random
import string

#password_dict = {}
#This should only create a password and not bother about where it's for


#The very Important function below, generates a 24 characyter strong password
#On a second thought, I have decdide to include some parameters into the password_gen, like website or app or whatever's name and probably the email
def password_generator(account_name,email):
  #account_name=str(input("Enter the account name, like oh, facebook:",))
  #email=str(input("Enter the email account if its associated with one, if not the enter 'none':",))
  upper_letters = string.ascii_uppercase
  lower_letters = string.ascii_lowercase
  digits = string.digits
  symbols = string.punctuation
  char = upper_letters + lower_letters + digits + symbols
  while True:
    a_random_string = ''.join(random.choices(char, k=20))
    if (sum(c.isupper() for c in a_random_string) >= 4 
        and sum(c.islower() for c in a_random_string) >= 3 
        and sum(c.isdigit() for c in a_random_string) >= 5
        and sum(c in symbols for c in a_random_string) >= 6):
      break
  return {"Password":a_random_string,"Account":account_name,"Email":email}
#The piece oof code directly, above is the returned normal password to be hashed below
password=password_generator("G-mail","None")

with open("passwords.txt", "a") as file:
    file.write(str(password))

#print(password["Password"])
#Below is the hashing process, this will be imported in the sqlite.py file, which is the database management stuff.
hashed_password=hashlib.sha256(password["Password"].encode()).hexdigest()
print(hashed_password)





'''def update_password(service_name, number_of_chars):
  new_password = password_generator(number_of_chars)
  password_dict[service_name] = new_password
  print(f"Password for {service_name} has been updated to: {new_password}")'''





