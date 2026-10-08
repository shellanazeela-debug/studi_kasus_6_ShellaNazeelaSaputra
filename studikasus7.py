import csv
import os

file = "implementasi.csv"

def clear():
    os.system("cls")

def lihat():
    clear()
    print("=== DATA BARANG ===")

    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                print(row)

    input("\nEnter untuk kembali...")

def tambah():
    clear()
    print("=== TAMBAH BARANG ===")

    id = input("ID Barang   : ")
    nama = input("Nama Barang : ")
    harga = input("Harga       : ")
    stok = input("Stok        : ")

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, nama, harga, stok])

    print("Data berhasil ditambahkan.")
    input("\nEnter untuk kembali...")

def hapus():
    clear()
    print("=== HAPUS BARANG ===")

    nomor = input("Masukkan ID barang: ")
    data = []

    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] != nomor:
                data.append(row)

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("Data berhasil dihapus.")
    input("\nEnter untuk kembali...")

while True:
    clear()
    print("=== SISTEM INVENTARIS ===")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Hapus Barang")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        lihat()
    elif pilihan == "2":
        tambah()
    elif pilihan == "3":
        hapus()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid.")
        input("\nEnter untuk kembali...")

