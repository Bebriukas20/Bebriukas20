import sys
from stdiomask import getpass
import hashlib
from sys import exit




def main():
    print("MAIN MENU")
    print("@@@@@@@@@@")
    print()
    print("1 - Register")
    print("2 - Login")
    print("3 - Exit")
    print()
    while True:
        print()
        pasirinkimas = input("Choose An Option: ")
        if pasirinkimas in ['1', '2', "3"]:
            break
    if pasirinkimas == '1':
        Register()
    elif pasirinkimas == "2":
        Login()
    else:
        sys.exit()  
        

def Register():
    print("REGISTER")
    print("--------")
    print()
    while True:
        vartotojoVardas = input("Enter Your Name: ").title()
        if vartotojoVardas != '' and vartotojoVardas != " " and vartotojoVardas.isalnum(): 
            break
    if vartotojasJauEgzistuoja(vartotojoVardas):
        zinuteKadVartotojasJauEgzistuoja()
    else:
        while True:
            userPassword = getpass("Enter Your Password: ")
            if userPassword != '' and userPassword != ' ':
                break
        while True:
            confirmPassword = getpass("Confirm Your Password: ")
            if confirmPassword == userPassword:
                break
            else:
                print("Passwords Don't Match")
                print()
        if vartotojasJauEgzistuoja(vartotojoVardas, userPassword):
            while True:
                print()
                error = input("You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
                if error == 't':
                    Register()
                    break
                elif error == 'l':
                    Login()
                    break
        pridetiVartotojoInfo([vartotojoVardas, hash_password(userPassword)])

        print()
        print("Registered!")

def Login():
    print("LOGIN")
    print("-----")
    print()
    usersInfo = {}
    with open('userInfo.txt', 'r') as f:
        for line in f:
            line = line.split()
            usersInfo.update({line[0]: line[1]})

    while True:
        vartotojoVardas = input("Enter Your Name: ").title()
        if vartotojoVardas not in usersInfo:
            print("You Are Not Registered")
            print()
        else:
            break
    while True:
        userPassword = getpass("Enter Your Password: ")
        if not check_password_hash(userPassword, usersInfo[vartotojoVardas]):
            print("Incorrect Password")
            print()
        else:
            break
    print()
    print("Logged In!")

def pridetiVartotojoInfo(userInfo: list):
    with open('userInfo.txt', 'a') as f:
        for info in userInfo:
            f.write(info)
            f.write(' ')
        f.write('\n')

def vartotojasJauEgzistuoja(vartotojoVardas, userPassword=None):
    if userPassword == None:
        with open('userInfo.txt', 'r') as f:
            for line in f:
                line = line.split()
                if line[0] == vartotojoVardas:
                    return True
        return False
    else:
        userPassword = hash_password(userPassword)
        usersInfo = {}
        with open('userInfo.txt', 'r') as f:
            for line in f:
                line = line.split()
                if line[0] == vartotojoVardas and line[1] == userPassword:
                    usersInfo.update({line[0]: line[1]})
        if usersInfo == {}:
            return False
        return usersInfo[vartotojoVardas] == userPassword

def zinuteKadVartotojasJauEgzistuoja():
    while True:
        print()
        error = input("You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
        if error == 't':
            Register()
            break
        elif error == 'l':
            Login()
            break

def vartotojoVardas(vartotojoVardas):
    vartotojoVardas = vartotojoVardas.split()
    vartotojoVardas = '-'.join(vartotojoVardas)
    return vartotojoVardas

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    return hash_password(password) == hash


main()
