import csv
import os

file = os.path.join(os.path.dirname(__file__), "implementasi.csv")

def lihat():
    print("=== DATA BARANG ===")
    if not os.path.exists(file):
        print("File CSV tidak ditemukan!")
        input("\nEnter untuk kembali...")
        return
    with open(file, "r", newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            if row:
                print("ID Barang   :", row[0])
                print("Nama Barang :", row[1])
                print("Harga       :", row[2])
                print("Stok        :", row[3])
                print()
    input("\nEnter untuk kembali...")


def tambah():
    print("=== TAMBAH BARANG ===")

    id_barang = input("ID Barang   : ")
    nama = input("Nama Barang : ")
    harga = input("Harga       : ")
    stok = input("Stok        : ")

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id_barang, nama, harga, stok])

    print("\nData berhasil ditambahkan!")
    input("\nEnter untuk kembali...")


while True:
    print("\n=== SISTEM INVENTARIS ===")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        lihat()
    elif pilihan == "2":
        tambah()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem inventaris.")
        break
    else:
        print("Pilihan tidak valid.")
        input("\nEnter untuk kembali...")


