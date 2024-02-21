sewa = []  # List untuk menyimpan informasi penyewaan saat ini
histori_penyewaan = []  # List untuk menyimpan histori penyewaan
liststock = [['Toyota', 'Yaris', 5, 2, 300000], ['Toyota', 'Camry', 5, 1, 500000], 
             ['Honda', 'HRV', 5, 3, 350000], ['Honda', 'CRV', 7, 4, 500000],
             ['Daihatsu', 'Xenia', 5, 2, 200000]]  # Data stok mobil

# Fungsi untuk melihat stok mobil
from tabulate import tabulate  # Mengimpor fungsi tabulate dari modul tabulate

# Fungsi untuk melihat stok mobil
def lihat_stock():
    if not liststock:  # Jika liststock kosong
        print('Stok mobil kosong.')  # Menampilkan pesan bahwa stok mobil kosong
    else:
        headers = ["Index", "Merek Mobil", "Tipe Mobil", "Kapasitas Mobil (orang)", "Stok Mobil", "Harga per hari"]  # Membuat header tabel
        table = [[i, *data] for i, data in enumerate(liststock)]  # Membuat list 2 dimensi dari data stok mobil
        print(tabulate(table, headers=headers))  # Mencetak tabel menggunakan fungsi tabulate dengan header yang telah ditentukan

# Fungsi untuk menambah mobil ke dalam stok
def tambah_mobil():
    print("Pilihan: ")
    print("1. Menambah stok mobil pada tipe yang ada")
    print("2. Menambah stok mobil tipe baru")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':  # Jika memilih untuk menambah stok pada tipe yang ada
        lihat_stock()
        index = int(input("Masukkan nomor indeks mobil yang ingin ditambah stoknya: "))
        if 0 <= index < len(liststock):
            tambah_stok = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
            liststock[index][3] += tambah_stok
            print("Stok mobil berhasil ditambahkan.")
        else:
            print("Indeks mobil tidak valid.")
    elif pilihan == '2':  # Jika memilih untuk menambah tipe mobil baru
        input_merek = input('Merek Mobil: ')
        input_tipe = input('Tipe Mobil: ')
        input_kapasitas = int(input('Kapasitas Mobil (orang): '))
        input_stok = int(input('Stok Mobil: '))
        input_harga = int(input('Harga per hari: '))
        liststock.append([input_merek, input_tipe, input_kapasitas, input_stok, input_harga])
        lihat_stock()
    else:
        print("Pilihan tidak valid.")

# Fungsi untuk menghapus mobil dari stok
def hapus_mobil():
    lihat_stock()
    if liststock:
        input_hapus = int(input('Silahkan masukkan index mobil yang ingin dihapuskan: '))
        if input_hapus in range(len(liststock)):
            del liststock[input_hapus]
            print('===== STOK TELAH DI UPDATE =====')
            print('Index \t| Merek Mobil \t| Tipe Mobil\t| Kapasitas Mobil (orang)\t| Harga per hari')
            for i in range(len(liststock)):
                print(f'{i:<6}|{liststock[i][0]:<13}|{liststock[i][1]:<12}|{liststock[i][2]:<27}|{liststock[i][3]:<11}|{liststock[i][4]}')
        else:
            print('Index tidak valid. Silakan pilih index yang sesuai.')


# Fungsi untuk menambahkan informasi penyewaan ke histori penyewaan
def tambah_ke_histori(mobil_disewa):
    histori_penyewaan.append(mobil_disewa)

# Fungsi untuk melihat histori penyewaan
def lihat_histori_penyewaan():
    if not histori_penyewaan:
        print("Belum ada histori penyewaan.")
    else:
        print("HISTORI PENYEWAAN:")
        for i in range(len(histori_penyewaan)):
            penyewaan = histori_penyewaan[i]
            print(f"Transaksi {i+1}:")
            print(f"  Nama: {penyewaan[5]}")
            print(f"  Nomor Telepon: {penyewaan[6]}")
            print(f"  Mobil: {penyewaan[0]} {penyewaan[1]}")
            print(f"  Tanggal Mulai Sewa: {penyewaan[8]}")
            print(f"  Jumlah Hari Sewa: {penyewaan[9]}")
            print(f"  Total Biaya: Rp {penyewaan[10]}")
            print()


# Fungsi untuk melakukan proses penyewaan mobil
def check_out():
    lihat_stock()
    print('\n')
    input_nama = str(input('Nama Anda: '))
    input_nomor_telfon = int(input('Silahkan masukkan nomor telfon anda: '))
    input_pilih_mobil = int(input('Silahkan masukkan No. Index dari mobil yang ingin di sewa: '))
    input_qty_mobil = int(input('Silahkan masukkan jumlah mobil yang ingin di sewa: '))
    input_tanggal_mulai = input('Silahkan masukkan tanggal mulai sewa (dd/mm/yyyy): ')
        
    if input_pilih_mobil not in range(len(liststock)):
        print(f'Index mobil yang Anda masukkan tidak ada dalam list stock')
        lihat_stock()
    elif input_qty_mobil > liststock[input_pilih_mobil][3]:
        print(f'Stok mobil tidak cukup, stok {liststock[input_pilih_mobil][1]} tinggal {liststock[input_pilih_mobil][3]}')
    else:
        # Hitung total biaya
        harga_per_hari = liststock[input_pilih_mobil][4]
        jumlah_hari = int(input('Silahkan masukkan jumlah hari penyewaan: '))
        total_biaya =input_qty_mobil * harga_per_hari * jumlah_hari
        
        # Masukkan ke list sewa
        mobil_disewa = liststock[input_pilih_mobil].copy()  # Copy informasi mobil yang disewa
        mobil_disewa.append(input_nama) #Menambahkan nama penyewa 5
        mobil_disewa.append(input_nomor_telfon) #Menambahkan nomor telfon 6
        mobil_disewa.append(input_qty_mobil)  # Menambahkan jumlah mobil yang disewa ke informasi mobil 7
        mobil_disewa.append(input_tanggal_mulai)  # Menambahkan tanggal mulai penyewaan 8
        mobil_disewa.append(jumlah_hari) # Menambahkan jumlah sewa hari 9
        mobil_disewa.append(total_biaya)  # Menambahkan total biaya 10
        sewa.append(mobil_disewa)  # Menambahkan ke list sewa
        tambah_ke_histori(mobil_disewa)
        
        # Update stok mobil
        liststock[input_pilih_mobil][3] -= input_qty_mobil
        
        if liststock[input_pilih_mobil][3] == 0:
            print(f'Stok mobil {liststock[input_pilih_mobil][0]} {liststock[input_pilih_mobil][1]} sudah habis.')
            print('Silakan pilih mobil lain atau tambahkan stok.')
            print('\n')
        
        print('===== PEMESANAN BERHASIL =====')
        print(f'Nama: {input_nama} No. Telp: {input_nomor_telfon}')
        print(f'Anda telah menyewa {input_qty_mobil} mobil {liststock[input_pilih_mobil][0]} {liststock[input_pilih_mobil][1]}')
        print(f'Tanggal mulai sewa: {input_tanggal_mulai}, Total biaya: Rp {total_biaya}')
        print('\n')

        #Pembayaran
        input_bayar = int(input('Silahkan jumlah yang ingin di bayarkan: '))
        while input_bayar >= total_biaya:
            kembali = input_bayar - total_biaya
            print(f'Terima kasih, kembali anda {kembali}. Mobil segera disiapkan!\n\n')
            sewa.clear()
            break
        else:
            print('Uang tidak cukup.\n\n')

# Main program
while True:
    print('Selamat Datang di Fabian Car Rental!\nAda yang bisa kami bantu?')
    print("\nPILIH MENU:")
    print("1. Lihat Stok Mobil")
    print("2. Tambah Mobil")
    print("3. Hapus Mobil")
    print("4. Check Out")
    print("5. Lihat Histori Penyewaan")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        lihat_stock()
    elif pilihan == '2':
        tambah_mobil()
    elif pilihan == '3':
        hapus_mobil()
    elif pilihan == '4':
        check_out()
    elif pilihan == '5':
        lihat_histori_penyewaan()
    elif pilihan == '6':
        print("Terima kasih. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
