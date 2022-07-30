import csv
import os

csv_filename = 'E:\Tugas Akhir martikulasi\scholarship.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI BEASISWA KIP ===")
    print("[1] Daftar Calon Beasiswa")
    print("[2] Buat Pendaftaran Baru")
    print("[3] Edit Pendaftaran")
    print("[4] Hapus Pendaftaran")
    print("[5] Cari Nama Pendaftar")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        show_scholarship()
    elif(selected_menu == "2"):
        create_scholarship()
    elif(selected_menu == "3"):
        edit_scholarship()
    elif(selected_menu == "4"):
        delete_scholarship()
    elif(selected_menu == "5"):
        search_scholarship()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_scholarship():
    clear_screen()
    scholarship = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            scholarship.append(row)

    if (len(scholarship) > 0):
        labels = scholarship.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        print("-"*34)
        for data in scholarship:
            print(f'{data[0]} \t {data[1]} \t {data[2]}')
    else:
        print("Tidak ada data!")
    back_to_menu()

def create_scholarship():
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NO', 'NAMA', 'NIM']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        no = input("No urut: ")
        nama = input("Nama lengkap: ")
        nim = input("No. NIM: ")

        writer.writerow({'NO': no, 'NAMA': nama, 'NIM': nim})
        print("Berhasil disimpan!")

    back_to_menu()

def edit_scholarship():
    clear_screen()
    scholarship = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            scholarship.append(row)

    print("NO \t NAMA \t\t NIM")
    print("-" * 32)

    for data in scholarship:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['NIM']}")

    print("-----------------------")
    no = input("Pilih nomer kontak> ")
    nama = input("nama baru: ")
    nim = input("nomer nim : ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in scholarship:
        if (data['NO'] == no):
            scholarship[indeks]['NAMA'] = nama
            scholarship[indeks]['NIM'] = nim
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'NIM']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in scholarship:
            writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'NIM': new_data['NIM']}) 

    back_to_menu()

def delete_scholarship():
    clear_screen()
    scholarship = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            scholarship.append(row)

    print("NO \t NAMA \t\t NIM")
    print("-" * 32)

    for data in scholarship:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['NIM']}")

    print("-----------------------")
    no = input("Hapus nomer> ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in scholarship:
        if (data['NO'] == no):
            scholarship.remove(scholarship[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'NIM']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in scholarship:
            writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'NIM': new_data['NIM']}) 

    print("Data sudah terhapus")
    back_to_menu()

def search_scholarship():
    clear_screen()
    scholarship = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            scholarship.append(row)

    no = input("Cari berdasrakan nomer urut> ")

    data_found = []

    # mencari nama pendaftar
    indeks = 0
    for data in scholarship:
        if (data['NO'] == no):
            data_found = scholarship[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Nama: {data_found['NAMA']}")
        print(f"nim: {data_found['NIM']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()
