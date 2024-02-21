#Fabian Car Rental
Fabian Car Rental adalah sebuah program sederhana untuk manajemen penyewaan mobil. Program ini memungkinkan pengguna untuk melakukan beberapa tindakan seperti melihat stok mobil, menambahkan mobil ke stok, menghapus mobil dari stok, melakukan proses penyewaan mobil, dan melihat histori penyewaan.

#Fungsi dan Fitur
#1. Melihat Stok Mobil (lihat_stock)
Fungsi ini memungkinkan pengguna untuk melihat stok mobil yang tersedia. Jika tidak ada mobil dalam stok, program akan memberikan pesan bahwa stok mobil kosong. Jika ada mobil dalam stok, tabel akan ditampilkan dengan informasi seperti merek, tipe, kapasitas, stok, dan harga per hari.

#2. Menambah Mobil (tambah_mobil)
Fitur ini memungkinkan pengguna untuk menambahkan mobil ke stok. Pengguna memiliki dua opsi: menambah stok pada tipe mobil yang sudah ada atau menambah tipe mobil baru. Jika pengguna memilih untuk menambah stok pada tipe mobil yang ada, mereka akan diminta untuk memilih nomor indeks mobil yang ingin ditambahkan stoknya dan memasukkan jumlah stok yang ingin ditambahkan. Jika pengguna memilih untuk menambah tipe mobil baru, mereka akan diminta untuk memasukkan informasi seperti merek, tipe, kapasitas, stok, dan harga per hari mobil baru.

#3. Menghapus Mobil (hapus_mobil)
Fitur ini memungkinkan pengguna untuk menghapus mobil dari stok. Pengguna akan diminta untuk memasukkan nomor indeks mobil yang ingin dihapus, dan mobil dengan indeks tersebut akan dihapus dari stok.

#4. Check Out (check_out)
Fitur ini memungkinkan pengguna untuk menyewa mobil. Pengguna akan diminta untuk memasukkan informasi seperti nama, nomor telepon, nomor indeks mobil yang ingin disewa, jumlah mobil yang ingin disewa, dan tanggal mulai sewa. Program akan memeriksa ketersediaan stok mobil dan menghitung total biaya penyewaan. Jika stok mencukupi, informasi penyewaan akan ditambahkan ke dalam daftar sewa, stok mobil akan diperbarui, dan total biaya akan ditampilkan. Pengguna kemudian diminta untuk melakukan pembayaran.

#5. Lihat Histori Penyewaan (lihat_histori_penyewaan)
Fungsi ini memungkinkan pengguna untuk melihat histori penyewaan mobil. Jika belum ada histori penyewaan, program akan memberikan pesan bahwa belum ada histori penyewaan. Jika histori penyewaan sudah ada, informasi tentang setiap transaksi penyewaan, seperti nama pelanggan, nomor telepon, mobil yang disewa, tanggal mulai sewa, jumlah hari sewa, dan total biaya, akan ditampilkan.

#Cara Menggunakan
Jalankan program dengan menjalankan file python fabian_car_rental.py.
Pilih opsi menu yang diinginkan dengan memasukkan angka yang sesuai.
Ikuti instruksi yang ditampilkan untuk setiap opsi menu.
Untuk menyewa mobil, pastikan untuk memilih opsi "Check Out" dan mengikuti instruksi yang ditampilkan untuk memasukkan informasi penyewaan.
Setelah selesai menggunakan program, pilih opsi "Keluar" untuk menutup program.
