
import os
os.system('cls')


print('='*21)
print("======Form Nama======")
print('='*21)

status = ''

def username():
    print()
    inputan = input("Masukkan Username: ")
    cek1 = len(inputan)
    cek2 = " " not in inputan
    cek3 = inputan[0].isupper()

    if cek1 > 10 and cek2 == True and cek3 == True:
        status = "Berhasil"
        return inputan, status
    else:
        inputan = "Username tidak valid"
        status = "Gagal"
        return inputan, status

def email():
    print()
    inputan = input("Masukkan Email: ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 ='@' and '.' in inputan

    if cek1 > 7 and cek2 == False and  cek3 == True:
        status = "Berhasil"
        return inputan, status

    else:
        inputan = "Email tidak valid"
        status = "Gagal"
        return inputan, status


def phone():
    print()
    inputan = input("Masukkan Nomor HP : ")
    cek1 = len(inputan)
    cek2 = " " in inputan
    cek3 = inputan.isdigit()
    
    if cek1 >= 12 and cek2 == False and cek3 == True:
        status = "Berhasil"
        return inputan, status

    else:
        inputan = "Email tidak Valid"
        status = "Gagal"
        return inputan, status

        
def main():
    while True:
        u1, u2 = username()
        print("\nUsername = ", u1)
        print("Status = ", u2)
        if u2 == "Berhasil":
            break

    while True:
        e1, e2 = email()
        print("\nEmail : ", e1)
        print("Status : ",e2)
        if e2 == "Berhasil":
            break

    while True:
        p1, p2 = phone()
        print("\nPhone : ", p1)
        print("Status : ",p2)
        if p2 == "Berhasil":
            break
main()





