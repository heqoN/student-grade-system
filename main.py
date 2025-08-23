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
        # Eğer dosya boş değilse satır sonu ekle
        if os.path.getsize("database.txt") > 0:
            file.write("\n")
        file.write(f"{name} {phone} {email} {passw}")
        print("  Başarıyla kayıt oldunuz .")

def login():
    email = input("  Emailinizi giriniz  >> ")
    passw = input("  Şifrenizi giriniz  >> ")
    with open("database.txt","r",encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:   # boş satır varsa atla
                continue
            parts = line.split()
            if len(parts) < 4:  # eksik satır varsa atla
                continue
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
        if os.path.getsize("scores.txt") > 0:
            file.write("\n")
        file.write(f"{number} {score}")
    print("  Notunuz sisteme girildi.")

def readScore():
    number = input("  Numaranızı giriniz >> ")
    found = False
    with open("scores.txt","r",encoding="utf-8") as file:
        for lines in file:
            lines = lines.strip()
            if not lines:
                continue
            parts = lines.split()
            if len(parts) < 2:
                continue
            storedNumber,score = parts
            if number == storedNumber :
                print(f"  Notunuz  >> {score}")
                found = True
    if not found:
        print("  Bu numara için not bulunamadı.")
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
