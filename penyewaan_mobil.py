from datetime import datetime

Mobil_tersedia = [
    { 'id': 426, 
     'merk': 'Toyota', 
     'model': 'Avanza', 
     'harga': 300000, 
     'tersedia': 4 },
    { 'id': 142, 
     'merk': 'Daihatsu', 
     'model': 'Ayla', 
     'harga': 250000, 
     'tersedia': 5 },
    { 'id': 534, 
     'merk': 'Honda', 
     'model': 'Brio', 
     'harga': 250000, 
     'tersedia': 4 },
    { 'id': 897, 
     'merk': 'Mitsubishi', 
     'model': 'Pajero', 
     'harga': 500000, 
     'tersedia': 3 }
]

penyewaan_terkini = {}

def tampilkan_mobil(Mobil_tersedia):
    print("\nMobil yang Tersedia untuk Disewa:")
    for i in Mobil_tersedia:
        if i['tersedia'] > 0:  
            print(f"ID          : {i['id']}")
            print(f"Merk        : {i['merk']}")
            print(f"Model       : {i['model']}")
            print(f"Harga       : Rp {i['harga']} per hari")
            print(f"Tersedia    : {i['tersedia']}")
            print("-" * 40)
        else:
            print(f"ID: {i['id']} - {i['merk']} {i['model']} - Tidak tersedia")

def hitung_total_harga(tanggal_sewa, tanggal_kembali, harga_per_hari, jumlah_mobil=1):

    format_tanggal = "%d-%m-%Y"
    tanggal_sewa = datetime.strptime(tanggal_sewa, format_tanggal)
    tanggal_kembali = datetime.strptime(tanggal_kembali, format_tanggal)

    durasi_sewa = (tanggal_kembali - tanggal_sewa).days
    if durasi_sewa < 0:
        print("Tanggal kembali tidak boleh lebih awal dari tanggal sewa.")
        return None
    
    total_harga = durasi_sewa * harga_per_hari * jumlah_mobil
    return total_harga

def pilih_metode_pembayaran(total_harga):
    while True:
        pembayaran = input("Pilih metode pembayaran (atm/cash): ").lower()
        
        if pembayaran == 'atm':
            pilih_atm = input("Masukkan jenis ATM apa yang anda miliki(MAN/BIN/RBI): ")
            
            if pilih_atm == "MAN":
                pajak = 0.05  
            elif pilih_atm == "BIN":
                pajak = 0.10  
            elif pilih_atm == "RBI":
                pajak = 0.15  
            else:
                print("Masukkan format yang benar (MAN/BIN/RBI).")
                continue
            
            total_dengan_pajak = total_harga + (total_harga * pajak)
            atm = int(input("Masukkan Nomor Rekening anda: "))
            print(f"Pembayaran menggunakan ATM berhasil. Total harga setelah pajak: Rp {total_dengan_pajak}")
            break 
            
        elif pembayaran == 'cash':
            while True:
                uang_diberikan = int(input(f"Masukkan nominal uang Anda: Rp "))
                
                if uang_diberikan < total_harga:
                    kekurangan = total_harga - uang_diberikan
                    print(f"Uang yang Anda berikan kurang sebanyak: Rp {kekurangan}. Silakan tambahkan uang.")
                
                elif uang_diberikan > total_harga:
                    kelebihan = uang_diberikan - total_harga
                    print(f"Uang yang Anda berikan lebih sebanyak: Rp {kelebihan}. Uang akan dikembalikan.")
                    break
                
                else:
                    print(f"Pembayaran dengan jumlah tepat. Terima kasih!")
                    break 
            
            print(f"Pembayaran dengan cash berhasil diterima. Terima kasih!")
            break  
            
        else:
            print("Metode pembayaran tidak valid. Pilih antara 'atm' atau 'cash'.")

def sewa_mobil():
    tampilkan_mobil(Mobil_tersedia)
    id_kendaraan = int(input("\nMasukkan ID mobil yang ingin disewa: ")) 

    Mobil = next((k for k in Mobil_tersedia if k['id'] == id_kendaraan and k['tersedia'] > 0), None)

    if not Mobil:
        print("Mobil tidak tersedia.")
        return
    
    nama_penyewa = input("Masukkan Nama Penyewa: ")
    tanggal_sewa = input("Masukkan tanggal sewa (dd-mm-yyyy): ")
    tanggal_kembali = input("Masukkan tanggal kembali (dd-mm-yyyy): ")

    total_harga = hitung_total_harga(tanggal_sewa, tanggal_kembali, Mobil['harga'])
    if total_harga is None:
        return

    while True:
        jumlah_mobil = int(input("Masukkan jumlah mobil yang ingin disewa: "))
        if jumlah_mobil <= 0:
            print("Jumlah mobil harus lebih dari 0.")
        elif jumlah_mobil > Mobil['tersedia']:
            print(f"Hanya ada {Mobil['tersedia']} mobil tersedia, coba sewa lebih sedikit.")
        else:
            break

    total_harga *= jumlah_mobil
    
    Mobil['tersedia'] -= jumlah_mobil
    print(f"Penyewaan berhasil! Total harga: Rp {total_harga}")

    penyewaan_terkini['mobil'] = Mobil
    penyewaan_terkini['nama_penyewa'] = nama_penyewa
    penyewaan_terkini['tanggal_sewa'] = tanggal_sewa
    penyewaan_terkini['tanggal_kembali'] = tanggal_kembali
    penyewaan_terkini['jumlah_mobil'] = jumlah_mobil
    penyewaan_terkini['total_harga'] = total_harga

    pilih_metode_pembayaran(total_harga)

def perbarui_penyewaan():
    if not penyewaan_terkini:
        print("Tidak ada penyewaan yang sedang berlangsung.")
        return

    print(f"\nPenyewaan terkini: {penyewaan_terkini['mobil']['merk']} {penyewaan_terkini['mobil']['model']} - Durasi: {penyewaan_terkini['jumlah_mobil']} unit")
    print(f"Nama Penyewa: {penyewaan_terkini['nama_penyewa']}")
    print(f"Tanggal Sewa: {penyewaan_terkini['tanggal_sewa']}")
    print(f"Tanggal Kembali: {penyewaan_terkini['tanggal_kembali']}")

    print("\nApa yang ingin Anda perbarui?")
    print("1. Perbarui Durasi Sewa")
    print("2. Batalkan Penyewaan")

    pilihan = input("Pilih opsi (1/2): ")

    if pilihan == "1":  
        tanggal_kembali = datetime.strptime(penyewaan_terkini['tanggal_kembali'], "%d-%m-%Y")  
        tanggal_kembali_baru = input("Masukkan tanggal kembali baru (dd-mm-yyyy): ")
        tanggal_kembali_baru = datetime.strptime(tanggal_kembali_baru, "%d-%m-%Y")

        durasi_tambahan = (tanggal_kembali_baru - tanggal_kembali).days
        if durasi_tambahan <= 0:
            print("Tanggal kembali tidak boleh lebih awal dari tanggal kembali yang lama.")
            return
        
        total_harga_tambahan = durasi_tambahan * penyewaan_terkini['mobil']['harga'] * penyewaan_terkini['jumlah_mobil']

        penyewaan_terkini['tanggal_kembali'] = tanggal_kembali_baru.strftime("%d-%m-%Y")
        penyewaan_terkini['total_harga'] += total_harga_tambahan

        print(f"Durasi tambahan berhasil diperbarui menjadi {durasi_tambahan} hari.")
        print(f"Total harga tambahan: Rp {total_harga_tambahan}")

        pilih_metode_pembayaran(total_harga_tambahan)

    elif pilihan == "2": 
        pembatalan = input("Apakah Anda yakin ingin membatalkan penyewaan? (ya/tidak): ")
        if pembatalan.lower() == "ya":
            penyewaan_terkini['mobil']['tersedia'] += penyewaan_terkini['jumlah_mobil']
            print("Jika batal menyewa, maka uang Anda tidak bisa dikembalikan.")
            print("Penyewaan berhasil dibatalkan.")
            penyewaan_terkini.clear()
        else:
            print("Penyewaan tidak dibatalkan. Kembali ke menu utama.")
    else:
        print("Opsi tidak valid. Kembali ke menu utama.")

def pengembalian_mobil():
    if not penyewaan_terkini:
        print("Tidak ada penyewaan yang sedang berlangsung.")
        return
    
    print(f"\nPenyewaan terkini: {penyewaan_terkini['mobil']['merk']} {penyewaan_terkini['mobil']['model']}")
    print(f"Nama Penyewa   : {penyewaan_terkini['nama_penyewa']}")
    print(f"Tanggal Sewa   : {penyewaan_terkini['tanggal_sewa']}")
    print(f"Tanggal Kembali: {penyewaan_terkini['tanggal_kembali']}")
    
    tanggal_kembali = datetime.strptime(penyewaan_terkini['tanggal_kembali'], "%d-%m-%Y")
    tanggal_kembali_sekarang = input("Masukkan tanggal pengembalian (dd-mm-yyyy): ")
    tanggal_kembali_sekarang = datetime.strptime(tanggal_kembali_sekarang, "%d-%m-%Y")
    
    if tanggal_kembali_sekarang > tanggal_kembali:
        terlambat = (tanggal_kembali_sekarang - tanggal_kembali).days
        denda = terlambat * penyewaan_terkini['mobil']['harga'] * penyewaan_terkini['jumlah_mobil']
        print(f"Anda terlambat {terlambat} hari. Denda yang dikenakan: Rp {denda}")
    
        if terlambat > 0:
            tarif_denda = 100000  
            biaya_denda = terlambat * tarif_denda
            print(f"Biaya tambahan (denda keterlambatan): Rp {biaya_denda}")
        else:
            biaya_denda = 0
            print("Mobil dikembalikan tepat waktu. Tidak ada denda keterlambatan.")
        pilih_metode_pembayaran(biaya_denda)
    else:
        print("Mobil dikembalikan tepat waktu atau lebih awal. Tidak ada denda.")
    
    penyewaan_terkini['mobil']['tersedia'] += penyewaan_terkini['jumlah_mobil']
    print(f"Mobil {penyewaan_terkini['mobil']['merk']} {penyewaan_terkini['mobil']['model']} berhasil dikembalikan.")
    
    penyewaan_terkini.clear()
    print("Penyewaan selesai. Terima kasih.")

def menu():
    while True:
        print("\n=================================")
        print("Selamat Datang Di Penyewaan Mobil")
        print("=================================")
        print("\n--- Daftar Menu Penyewaan ---")
        print("1. Tampilkan Mobil yang Tersedia")
        print("2. Sewa Mobil berdasarkan ID")
        print("3. Perbarui Penyewaan")
        print("4. Pengembalian Mobil")
        print("5. Keluar")

        pilihan = input("Pilih menu yang kamu inginkan(1/2/3/4/5): ")
        if pilihan == "1":
            tampilkan_mobil(Mobil_tersedia)
        elif pilihan == "2":
            sewa_mobil()
        elif pilihan == "3":
            perbarui_penyewaan()
        elif pilihan == "4":
            pengembalian_mobil()
        elif pilihan == "5":
            print("\n=======================================")
            print("Terimakasih Telah Menggunakan Jasa Kami")
            print("=======================================")
            break  
        else:
            print("Pilih salah satu angka diatas")

if __name__ == "__main__":
    menu()
