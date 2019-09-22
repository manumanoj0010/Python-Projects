import random
import pickle


def generator(s,len_password): 
    password="".join(random.sample(s,len_password))
    print(password)

    user_input=input("Would you like to keep this password:")
    if(user_input.lower()=="yes"):
        account_name=input("Enter your account name for storing the password:")
        if(account_name.strip()==''):
            print("Accoount Name should not be empty")
        else:
            passwords[account_name]=password
            with open("secure.abs","bw") as filee:  #bw = binary write file
                pickle.dump(passwords,filee,protocol=2)

    else:
        print("Try for another password")

#creating a empty dictionary
passwords={}

s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=,./;[]`~"

small_letters='abcdefghijklmnopqrstuvwxyz'
capital_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='1234567890'
special_characters='!@#$%^&*()_-+=,./;[]`~'


len_password=int(input("Enter number of letters in password:"))
answer=input("Do you want to include all the captials, small and special characters?:")
if(answer.lower()=="yes"):
    generator(s,len_password)

else:
    capitals=input("Would you like to include captial letters:")
    numbers=input("Would you like to include numbers:")
    special=input("would you like to include special characters:")

    if(capitals.lower()=='yes' and special.lower()=="yes" and numbers.lower()=='yes' ):
        generator(s,len_password)

    elif(capitals.lower()=="yes" and special.lower()=="yes" and numbers.lower()=='no'):
        new_s=small_letters+capital_letters+special_characters
        generator(new_s,len_password)

    elif(capitals.lower()=="yes" and special.lower()=="no" and numbers.lower()=='yes'):
        new_s=small_letters+capital_letters+numbers
        generator(new_s,len_password)

    elif(capitals.lower()=="yes" and special.lower()=="no" and numbers.lower()=='no'):
        new_s=small_letters+capital_letters
        generator(new_s,len_password)

    elif(capitals.lower()=="no" and special.lower()=="yes" and numbers.lower()=='yes'):
        new_s=small_letters+special_characters+numbers
        generator(new_s,len_password)

    elif(capitals.lower()=="no" and special.lower()=="no" and numbers.lower()=='yes'):
        new_s=small_letters+numbers
        generator(new_s,len_password)

    elif(capitals.lower()=="no" and special.lower()=="yes" and numbers.lower()=='no'):
        new_s=small_letters+special_characters
        generator(new_s,len_password)

    elif(capitals.lower()=="no" and special.lower()=="no" and numbers.lower()=='no'):
        new_s=small_letters
        generator(new_s,len_password)


        
