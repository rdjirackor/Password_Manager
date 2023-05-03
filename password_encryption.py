from cryptography.fernet import Fernet


password_dict = {"password": "password", "account_for": "account_name", "name_of_user_in_particular": "name", "time": "timestamp"}

key = Fernet.generate_key()
fernet = Fernet(key)
encrypted_password = {"Password": fernet.encrypt(password_dict["password"].encode()), "account_for": password_dict["account_for"], "name_of_user_in_particular": password_dict["name_of_user_in_particular"], "time": password_dict["time"]}

with open("encrypted_passwords", "a") as file:
    file.write(str(encrypted_password))
