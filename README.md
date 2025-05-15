# Capstone1 PWDK - PythonFundamental
# 🛵 XYZ Rental Motor - Sistem Penyewaan Motor Sederhana

Proyek ini merupakan aplikasi terminal sederhana yang dibuat dengan Python untuk mengelola penyewaan motor pada rental. Aplikasi ini memungkinkan pengguna untuk melihat, menambah, menghapus, dan menyewa motor, serta melakukan pembayaran dengan rekap transaksi yang rapi.

## 📌 Fitur Utama

- ✅ **Lihat Daftar Motor**: Menampilkan daftar motor yang tersedia beserta detailnya.
- ➕ **Tambah Motor**: Menambahkan motor baru ke dalam sistem.
- ❌ **Hapus Motor**: Menghapus motor dari daftar berdasarkan index.
- 🛒 **Sewa Motor**: Melakukan proses penyewaan motor, mengurangi stok, dan mencatat lamanya sewa.
- 🧾 **Rekap & Pembayaran**: Menampilkan ringkasan transaksi dan menghitung total biaya dan kembalian.

## ⚙️ Teknologi yang Digunakan

- Python 3
- Library: [`tabulate`](https://pypi.org/project/tabulate/) – Untuk menampilkan data dalam bentuk tabel di terminal

## ▶️ Cara Menjalankan Aplikasi

1. **Clone repository atau unduh file `.py`**
2. **Install library `tabulate` jika belum terpasang**:
   ```bash
   pip install tabulate
2. **Jalankan program di terminal:**:
   ```bash
   python Immaculata\ Viandra_Capstone\ M1.py

## 📂 Struktur File
```bash
      .
   ├── Immaculata Viandra_Capstone M1.py   # Script utama aplikasi
   └── README.md                           # Dokumentasi proyek

## Contoh Tampilan 
Menu Utama:
=== Selamat Datang di XYZ Rental Motor ===
1. Lihat Daftar Motor
2. Tambah Motor
3. Hapus Motor
4. Sewa Motor
5. Keluar

Tabel Daftar Motor:
+---------+--------------+---------+--------------+---------+
| Index   | Merk Motor   | Stock   | Tipe Motor   | Harga   |
+=========+==============+=========+==============+=========+
| 0       | Yamaha       | 3       | Matic        | 50000   |
| 1       | Honda        | 5       | Sport        | 60000   |
+---------+--------------+---------+--------------+---------+

📌 Catatan
1. Aplikasi ini hanya berbasis CLI/terminal.
2. Belum terdapat penyimpanan permanen (data tidak disimpan setelah program ditutup).
3. Program cocok untuk latihan CRUD dan logika transaksi dasar dalam Python.
