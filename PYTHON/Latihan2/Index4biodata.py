# Membuat Biodata

# Membuat variabel nama_saya yang menerima inputan
nama_lengkap = input("Masukkan Nama Lengkap : ")

# Membuat variabel asal_daerah yang menerima inputan
asal_daerah = input("Masukkan Asal Daerah : ")

# Membuat variabel array biodata untuk mengumpulkan hasil inputan
biodata = [ nama_lengkap, asal_daerah ]

no = 0
for isi_biodata in biodata :
    print(biodata[no])
    no = no + 1
    