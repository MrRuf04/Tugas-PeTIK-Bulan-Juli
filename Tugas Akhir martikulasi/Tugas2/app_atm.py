import os
import random, string
os.system('cls')

user_id = 0
loop = "n"
users = [
    {
        "id": "1",
        "no_rekening": "1234567890",
        "username": "Amar Ma'ruf",
        "pin": "4321",
        "saldo": 32000000
    },

    {
        "id": "2",
        "no_rekening": "0987654321",
        "username": "maulana",
        "pin": "1234",
        "saldo": 26000000
    },
    {
        "id": "3",
        "no_rekening": "0987654765",
        "username": "Elki",
        "pin": "1111",
        "saldo": 2000000
    }
]



status_login = False
pakai_atm = "y"


def cek_login(p):
    for user in users:
        if user['pin'] == p:
            return user
    return False


def cek_user(id):
    for i in range(len(users)):
        if users[i]['id'] == str(id):
            return int(i)
    return -1


def cek_rekening(no):
    for i in range(len(users)):
        if str(users[i]['no_rekening']) == str(no):
            return int(i)
    return -1


def tranfer_uang(uang, no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            users[index2]['saldo'] = users[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp." + str(uang) + " ke Rekening " + no_rekening)
            print("sisa saldo anda adalah Rp.", users[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")
        return users[index1]['saldo']


def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            print("Anda berhasil menarik uang Rp." + str(uang))
            print("sisa saldo anda adalah Rp.", users[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")


while pakai_atm == "y":
    while not status_login:
        print("SELAMAT DATANG DI ATM BANK PeTIK")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")

        cl = cek_login(pin)
        if cl:
            print("selamat datang " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ops PIN anda salah")
            print("")
            print("")

    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print("SELAMAT DATANG DI ATM PeTIK")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        no_rek = ""
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.", u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rek)

            if cnk >= 0:
                print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                nominal = input("Nominal Yang Akan Di Transfer : ")
                tranfer_uang(nominal, no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"

        elif a == 3:
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False

        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
            break
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"


