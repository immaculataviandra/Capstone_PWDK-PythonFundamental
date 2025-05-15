from tabulate import tabulate

# data awal disesuaikan dengan struktur yang konsisten
daftarmotor = {
    "motor1": {"merk": "Yamaha", "tipe": "Matic", "stock": 3, "harga": 50000},
    "motor2": {"merk": "Honda", "tipe": "Sport", "stock": 5, "harga": 60000}
}

pesanan = []

# 1. READ
def tampilkan_motor(daftarmotor):
    print("\nDaftar Motor Yang Tersedia")
    list_motor = []
    for i, (_, motor) in enumerate(daftarmotor.items()):
        list_motor.append([
            i,
            motor['merk'],
            motor['stock'],
            motor['tipe'],
            motor['harga']
        ])
    print(tabulate(list_motor, headers=["Index", "Merk Motor", "Stock", "Tipe Motor", "Harga"], tablefmt="grid"))

# 2. CREATE
def tambah_motor(daftarmotor):
    while True:
        motorbaru = input("\nTambahkan Merk motor ke Gudang: ").capitalize()
        tipebaru = input("Tipe Motor (Matic/Sport/Gigi dll): ").capitalize()

        if any(motor['merk'].lower() == motorbaru.lower() and motor['tipe'].lower() == tipebaru.lower() for motor in daftarmotor.values()):
            print("→ Tipe motor sudah ada dalam daftar.")
            continue

        stockbaru = int(input("Stock Motor: "))
        hargabaru = int(input("Harga sewa: "))

        index_baru = f"motor{len(daftarmotor) + 1}"
        daftarmotor[index_baru] = {
            "merk": motorbaru,
            "tipe": tipebaru,
            "stock": stockbaru,
            "harga": hargabaru
        }
        print(f"→ Motor '{motorbaru}' ditambahkan sebagai {index_baru}.")
        break

# 3. DELETE
def hapus_motor(daftarmotor):
    tampilkan_motor(daftarmotor)
    list_motor = list(daftarmotor.items())
    while True:
        try:
            index_hapus = int(input("\nMasukkan index motor yang ingin dihapus: "))
            kode_hapus = list_motor[index_hapus][0]
            del daftarmotor[kode_hapus]
            print(f"→ Motor '{kode_hapus}' berhasil dihapus dari daftar.")
            break
        except (IndexError, ValueError):
            print("→ Index tidak valid. Silakan coba lagi.")

# 4. UPDATE | Menyewa motor
def sewa_motor(daftarmotor):
    while True:
        print("\nDaftar Sewa Motor XYZ")
        list_motor = list(daftarmotor.items())
        tabel = []

        for i, (_, value) in enumerate(list_motor):
            tabel.append([i, value['merk'], value['stock'], value['tipe'], value['harga']])

        print(tabulate(tabel, headers=["Index", "Merk Motor", "Stock", "Tipe Motor", "Harga per Jam"], tablefmt="grid"))

        try:
            idx = int(input("Masukkan index motor yang disewa: "))
            if idx < 0 or idx >= len(list_motor):
                print("→ Index tidak tersedia. Silakan coba lagi.")
                continue

            qty = int(input("Jumlah motor yang disewa: "))
            kode_motor, value = list_motor[idx]

            if qty > value["stock"]:
                print(f"→ Sisa stock untuk {value['merk']}: {value['stock']}. Silahkan input ulang.")
                continue

            lamasewa = int(input("Berapa jam Anda ingin menyewa motor ini? "))

            daftarmotor[kode_motor]["stock"] -= qty
            total = value["harga"] * qty * lamasewa
            pesanan.append({
                "merk": value["merk"],
                "jumlah": qty,
                "tipe": value["tipe"],
                "lamasewa": lamasewa,
                "harga": value["harga"],
                "total": total
            })
            print(f"→ Anda menyewa {qty} unit {value['merk']} selama {lamasewa} jam (Total: Rp{total})")

        except ValueError:
            print("→ Input harus berupa angka. Silakan coba lagi.")
            continue

        lagi = input("Mau sewa motor lain? (ya/tidak): ").strip().lower()
        if lagi != "ya":
            break

    rekap_pesanan(pesanan)

# 5. REKAP
def rekap_pesanan(pesanan):
    if not pesanan:
        print("\nTidak ada motor yang disewa.")
        return

    print("\nRekap Sewa Motor Anda:")
    tabel = []
    total_semua = 0
    for item in pesanan:
        tabel.append([
            item["merk"],
            item["jumlah"],
            item["tipe"],
            item["lamasewa"],
            item["harga"],
            item["total"]
        ])
        total_semua += item["total"]

    print(tabulate(tabel, headers=["Merk", "Jumlah", "Tipe Motor", "Lama Sewa (per jam)", "Harga per Unit & per Jam", "Total"], tablefmt="grid"))
    print(f"\nTotal keseluruhan sewa: Rp{total_semua}")
    bayar(total_semua)

# 6. BAYAR
def bayar(total):
    while True:
        try:
            uang = int(input("Masukkan uang Anda: "))
            if uang < total:
                print(f"→ Uang kurang Rp{total - uang}. Silakan ulangi.")
            else:
                kembali = uang - total
                if kembali > 0:
                    print(f"→ Kembalian Anda: Rp{kembali}")
                print("→ Terima kasih sudah menyewa motor di XYZ Rental!")
                break
        except ValueError:
            print("→ Masukkan harus berupa angka.")

# 7. MAIN MENU
def main():
    while True:
        print("\n=== Selamat Datang di XYZ Rental Motor ===")
        print("1. Lihat Daftar Motor")
        print("2. Tambah Motor")
        print("3. Hapus Motor")
        print("4. Sewa Motor")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tampilkan_motor(daftarmotor)
        elif pilihan == "2":
            tambah_motor(daftarmotor)
        elif pilihan == "3":
            hapus_motor(daftarmotor)
        elif pilihan == "4":
            sewa_motor(daftarmotor)
        elif pilihan == "5":
            print("→ Terima kasih. Sampai jumpa!")
            break
        else:
            print("→ Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
main()
