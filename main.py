import sys 
import os 

def create_files():
    if not os.path.exists("database.txt"):
        with open("database.txt", "w", encoding="utf-8") as file:
            pass 

    if not os.path.exists("scores.txt"):
        with open("scores.txt", "w", encoding="utf-8") as file:
            pass 
create_files()

def register():
    with open("database.txt","a",encoding="utf-8") as file:
        name = input("  Adınız  >> ")
        phone = input("  Telefon numaranız  >> ")
        email = input("  Email adresiniz  >> ")
        passw = input("  Şifreniz  >> ")
        file.write(f"\n{name} {phone} {email} {passw}")
        print("  Başarıyla kayıt oldunuz .")

def login():
    email = input("  Emailinizi giriniz  >> ")
    passw = input("  Şifrenizi giriniz  >> ")
    with open("database.txt","r",encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            storedName,storedPhone,storedEmail,storedPassw = parts
            if email == storedEmail and passw == storedPassw :
                print(f"  Hoşgeldin {storedName}. Başarıyla giriş yaptınız.")
                return True
    print("  Email veya parola yanlış.")
    return False

def writeScore():
    number = input("  Numaranızı giriniz  >> ")
    score = input("  Notunuzu giriniz  >> ")
    with open("scores.txt","a",encoding="utf-8") as file:
        file.write(f"\n{number} {score}")
    print("  Notunuz sisteme girildi.")

def readScore():
    number = input("  Numaranızı giriniz >> ")
    with open("scores.txt","r",encoding="utf-8") as file:
        for lines in file:
            parts = lines.strip().split()
            storedNumber,score = parts
            if number == storedNumber :
                print(f"  Notunuz  >> {score}")
    print("by heqoN".center(100,"-"))




print("by heqoN".center(100,"-"))

islem1 = int(input("  Kayıt olmak için      -1 \n  Giriş yapmak için     -2 \n\n   >>> "))

if islem1 == 1 :
    register()
elif islem1 == 2 :
    result = login()
    if result == False :
        sys.exit()
    else:
        islem2 = int(input("  Not girmek için -1 \n  Not görmek için -2\n\n   >>> "))
        if islem2 == 1 :
            writeScore()
            sys.exit()
        if islem2 == 2 :
            readScore()

