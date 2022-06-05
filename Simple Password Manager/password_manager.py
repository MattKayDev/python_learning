import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import  PBKDF2HMAC

key = b"key"

def hash_password(password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    bpassword = str.encode(password)
    new_key = base64.urlsafe_b64encode(kdf.derive(bpassword))
    return new_key

def write_key(password):
    key = hash_password(password)
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    print('Master Password has been saved')

def load_key():
    with open('key.key',"rb") as key_file:
        key = key_file.read()
    return key

print("Do you want to `Login` using Master Password or `Create` new Master Password?")
print("When you create a new one it will scramble any passwords that have already been saved.")
q1 = input("`Login` or `Create`:  ")
master_pwd = ""
if q1.lower() == "login":
    master_pwd = input("What is the Master Password? :")
    key_loaded = load_key()
    key_to_check = hash_password(master_pwd)    
    if key_loaded == key_to_check:
        key = key_loaded
        print("Logged in successfully")
    else:
        print("Wrong password.")
        quit()
elif q1.lower() == "create":
    master_pwd = input("What would you like the Master Password to be? :")
    write_key(master_pwd)
else:
    quit()

def view():
    with open ('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    fer = Fernet(key)
    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add or view exisiting ones? Type view to view passwords, add to add new password or q to quit?")
    if mode == "q":
        break    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")