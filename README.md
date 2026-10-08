Nama : Shella Nazeela Saputra<br>
Nim :2609116018<br>

**======== LAPORAN STUDI KASUS 6 ========** <br>
1. Import CSV Dan Import OS<br>
<img width="107" height="27" alt="Screenshot 2026-10-08 185550" src="https://github.com/user-attachments/assets/3db35752-56ac-4ef3-ac87-510b8fe9224d" /> <br>
`import csv` digunakan untuk import code csv yang berguna untuk membaca dan menulis data pada file CSV. dan untuk `Import OS` digunakan untuk import fungsi os yang berfungsi untuk mengecek keberadaan file CSV.<br>

2.<img width="460" height="34" alt="Screenshot 2026-10-08 185557" src="https://github.com/user-attachments/assets/d48ac378-764c-40e0-a9e2-04e71690c106" /> <br>
Digunakan untuk menentukan lokasi file `implementasi.csv` agar program dapat menemukan dan mengakses file tersebut di folder yang sama dengan program Python.  <br>

3.<img width="293" height="212" alt="Screenshot 2026-10-08 191430" src="https://github.com/user-attachments/assets/f8b0be15-7f0f-474c-a0b7-3424fde46524" /> <br>
Fungsi `lihat()`  digunakan untuk membaca dan menampilkan data barang dari file CSV. Program terlebih dahulu menampilkan judul, kemudian mengecek apakah file CSV tersedia menggunakan `os.path.exists(file)`. Jika file tidak ditemukan, program menampilkan pesan dan menghentikan fungsi dengan return. Jika file tersedia, `open(file, "r", newline="")` digunakan untuk membuka file dalam mode membaca, lalu `csv.reader(f)` membaca data CSV baris demi baris. Setiap baris yang tidak kosong akan ditampilkan berdasarkan kolomnya, yaitu `row[0]` untuk ID barang, `row[1]` untuk nama barang, `row[2]` untuk harga, dan `row[3]` untuk stok. Setelah semua data ditampilkan, input() digunakan untuk menunggu pengguna menekan Enter sebelum kembali ke menu.<br>

4.<img width="353" height="170" alt="Screenshot 2026-10-08 185638" src="https://github.com/user-attachments/assets/724b36c4-3f03-45db-ad28-26266cc49aff" /> <br>
Fungsi `tambah()` digunakan untuk menambahkan data barang baru ke dalam file CSV secara permanen. Program menampilkan judul, kemudian meminta pengguna memasukkan ID barang, nama barang, harga, dan stok menggunakan `input()`. Setelah data dimasukkan, `open(file, "a", newline="")` membuka file CSV dan data baru ditambahkan di akhir file tanpa menghapus data sebelumnya. Selanjutnya, `csv.writer(f)` digunakan untuk menulis data ke CSV dan `writer.writerow([id_barang, nama, harga, stok])` menyimpan data tersebut sebagai satu baris baru. Setelah berhasil, program menampilkan pesan bahwa data telah ditambahkan dan `input()` digunakan untuk menunggu pengguna menekan Enter.<br>

5. <img width="440" height="216" alt="Screenshot 2026-10-08 193717" src="https://github.com/user-attachments/assets/2a2202bd-8665-4f19-8bdb-621b490cdf01" /> <br>
Bagian program tersebut digunakan untuk menampilkan menu utama dan mengatur pilihan pengguna dalam sistem inventaris. `while True` membuat menu terus berjalan sampai pengguna memilih keluar. Program menampilkan tiga pilihan, yaitu melihat barang, menambah barang, dan keluar, kemudian `input()` digunakan untuk menerima pilihan pengguna. Jika pilihan "1", fungsi `lihat()` dijalankan untuk menampilkan data barang, jika "2" maka fungsi `tambah()` dijalankan untuk menambahkan data, sedangkan jika "3" program menampilkan pesan terima kasih dan break digunakan untuk menghentikan perulangan. Jika pengguna memasukkan pilihan selain 1, 2, atau 3, program menampilkan pesan “Pilihan tidak valid” dan meminta pengguna menekan Enter untuk kembali ke menu.<br>

6.<img width="211" height="114" alt="Screenshot 2026-10-08 194812" src="https://github.com/user-attachments/assets/e3ba20fe-5701-4582-aabd-de6059d7bbc0" /> <br>
Bagian ini merupakan isi data dari file `implementasi.csv` File CSV tersebut berisi data inventaris barang toko kelontong yang terdiri dari empat kolom, yaitu ID, Nama Barang, Harga, dan Stok. <br>

**OUTPUT**<BR>
<img width="218" height="432" alt="Screenshot 2026-10-08 195100" src="https://github.com/user-attachments/assets/a94893aa-262d-4479-9272-b88a110ed965" /> <BR>
<img width="175" height="112" alt="image" src="https://github.com/user-attachments/assets/62c6c545-5a8a-4320-9095-99568d579d79" /> <BR>
<img width="350" height="103" alt="Screenshot 2026-10-08 195527" src="https://github.com/user-attachments/assets/ebbc7bda-ae19-4807-8a33-aac1725fd700" /> <BR>
<img width="310" height="320" alt="Screenshot 2026-10-08 195516" src="https://github.com/user-attachments/assets/faaca1b3-b84a-4c51-bf33-c33fb1946dd6" /> <BR>








