# tugas kelompok
# silahkan buat satu aplikasi sederhana  (cth. kalkulator, dll....)
# if else, while/for, input output
# tulis komentar disetiap blok/statement aplikasi
# presentasi kodingan
# demo-kan aplikasi tersebut

# inputan nama, golongan, jam kerja, gaji pokok
print()
print()
print("============Aplikasi Gaji Karyawan YBM PLN=============")
print("Kelompok :"," \n1. Amar Ma'ruf  "," \n2. Hanif Al-Faruq")
print("=======================================================")
print()
print("==Proses Perhitungan Gaji Karyawan YBM PLN==")
while (True) :

    nama = str(input("Masukkan nama penerima Gaji: "))
    gol = input ("golongan : ")
    jam = int (input("Masukkan jumlah jam : "))
    gaji = 300000
    tunjangan = ""
    
    if gol == "1"   : 
        upah = 0.05*gaji
    elif gol == "2" :
        upah = 0.10*gaji
    elif gol == "3":
        upah = 0.15*gaji
    else:
        print("tidak ada golongan")
    # Menghitung rumus
    if jam >= 48 :
        lembur = jam - 48
        tunjangan = 48 * upah + lembur * 20000
    else :
        tunjangan = jam * upah

    print (tunjangan)
    print("==Proses Penerimaan Gaji Melalui Bank Terdekat==")
    transfer = input("Transfer melalui : ")
    tujuan = input("Nama Tujuan: ")
    print("+---BANK BRI---+")
    print("Pilih Option :")
    print("1. Check Saldo")
    print("2. Mengambil Uang ")
    print("3. Tabung Uang ")
    print("4. Transfer Uang ")
    print("+----------------------+")

    option4 = ""
    hasil4=""
    saldo=""
    option=int(input("Silahkan Pilih Option :"))
    if option==1:
        print("Saldo Bejumlah Rp.22.000.000")
    elif option==2:
        print("$-----------------------------------------------$")
        print("Saldo Berjumlah Rp.22.000.000,\npilihan")
        print("1. Rp.200.000")
        print("2. Rp.500.000")
        print("3. pilihan lain : ",gol)
        saldo=22000000.0
        
        option2=int(input("Option :"))
        if option2==1:
            hasil=("",saldo-gaji)
            print("Saldo Berjumlah :",hasil)
        else:
            print("xxxxx--->Keyword Anda Salah!<---xxxxx")
    elif option==3:
        saldo=22000000.0     
        print("Saldo berjumlah Rp.22.000.000, Mau Nabung Berapa?") 
        
        option3=int(input("Masukkan Jumlah Uang :"))
        
        hasil3=saldo+option3
        print("Jumlah Uang Kamu Sekarang Adalah ",hasil3) 
    elif option==4:
        saldo=22000000.0
        print("Saldo Bejumlah Rp.22.000.000,Jumlah Transfer ?")
        option4=float(input("Masukkan Jumlah Uang diTransfer: "))
        hasil4=saldo-tunjangan
        print("Uang Terkirim ke Nama tujuan: ",tujuan)
        print("Sisa Saldo anda :",hasil4)
    else:
        print("xxxxx--->Keyword Anda Salah, Mohon Coba Lagi!<---xxxxx") 
    gaji == gol

    status = input("Apakah masih ada yang ingin di input? (y = ya, n = tidak)?")
    if status == "n" :
        print("Program Berhenti")
        break
    elif status == "y" :
        print("Silahkan Input Kembali Data") 

    else :
        print("Inputan Tidak Di Kenali")
        break

print()
print("==========Good Job =========")
print()

# Variabel bon berfungsi memasukkan data kedalam bon.txt untuk membuat stuktur/bon
# terdapat "file=bon" yang berfungsi memindahkan tulisan kedalam file bon.txt
bon = (open("bon.txt", "w"))
print("-------------------------------------",file=bon)
print("$++============BANK BRI===========++$",file=bon)
print("-------------------------------------",file=bon)
print(file=bon)
print("Nama Tujuan      : ",  tujuan,file=bon)
print("Transfer Melalui : ",  transfer,file=bon)
print("Saldo            : ",  saldo,file=bon)
print("Uang Terkirim    : ",  option4,file=bon)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",file=bon) 
print("Sisa Saldo       : ",  hasil4,file=bon)
print(file=bon)
print("-------------------------------------",file=bon)
print("$$$$$-------  THANK YOU   ------$$$$$",file=bon)
print("-------------------------------------",file=bon)
print(file=bon)
bon.close()# bon.close berfungsi penutup dari varaiabel bon


