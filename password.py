import string
import random
from cryptography.fernet import Fernet

def gen_random_pw():
    global final_pw
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    length = int(input("Enter Password Length :- "))
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    final_pw = ("".join(password))

def encrypt(key,message):
    alpha = string.ascii_letters
    result = ""

    for letter in message:
        if letter in alpha: # ABCabc
            letter_index = (alpha.find(letter) + key) % len(alpha)
            #print(letter_index)

            result = result + alpha[letter_index]
            #print(f"ALPHA :- {result}")
        else:
            result = result + letter

    return result

def decrypt(key,message):
    alpha = string.ascii_letters
    result = ""

    for letter in message:
        if letter in alpha: # ABCabc
            letter_index = (alpha.find(letter) - key) % len(alpha)
            #print(letter_index)

            result = result + alpha[letter_index]
            #print(f"ALPHA :- {result}")
        else:
            result = result + letter

    return result

def main():
    a = int(input("Do You Want to Save [1] or Fetch [2] a Password "))
    if (a==1):
        app_web = input("For Which Website/App Is this Password For :- ")
        gen_random_pw()
        print(final_pw)

        enc = encrypt(5,f"{app_web} --> {final_pw}")

        file = open("password.txt","a")
        file.write(f"{enc}\n")
        file.close()

    else:
        file = open("password.txt","r")
        content = file.read()
        dec = decrypt(5,content)
        print(dec)
        file.close()


