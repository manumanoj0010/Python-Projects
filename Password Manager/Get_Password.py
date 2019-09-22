import pickle
import pyperclip

master_password=input("Enter your master password:")

if(master_password=='Password'):
    account_name=input("Enter account name:")
    with open('secure.abs','br') as filee:
        passwords=pickle.load(filee)

    if account_name in passwords:
        pyperclip.copy(passwords[account_name])
        print("Password copied")
    else:
        print("Password not found")
else:
    print("Incorrect password")
