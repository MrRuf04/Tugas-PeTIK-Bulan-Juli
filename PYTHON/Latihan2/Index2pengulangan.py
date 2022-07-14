print('A' , 1, 'XYZ' , 2)
print('Nama Saya Amar Maruf')
print('Pesan Saya, Tetap Semangat jangan lupa Besyukur')


siswa = []
daerah = []
# i = index

#membuat perulangan angka 5 sampai 9 jika mau sampai no.10 + 1 contoh: i+1

# perulangan angka
for i in range(4):

    # mengecek nilai index
    print("ini adalah index ke-",i+1)

    #menerima inputan nama dan daerah
    nama_siswa = input("Masukkan nama siswa : ")
    nama_daerah = input("Masukkan nama daerah : ")

    #memasukkan hasil inputan nama dan daerah ke array siswa dan daerah
    siswa.append(nama_siswa)
    daerah.append(nama_daerah)
    
# membuat perulangan untuk mencetak data dari array siswa dan daerah
for j in siswa:
    print("Nama siswa = ",j)
for k in daerah:
    print("Nama daerah = ",k)


    # Membuat nomor berisikan urutan nomor 1-10 berisikan angka yang kita inginkan
    


