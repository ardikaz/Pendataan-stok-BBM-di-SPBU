# Kelas B, Kelompok 1
Anggota :
1. Ardika Tri Purnama (I0324073)
2. Fangkhu Ari Wijaya (I0324079)
3. Muhammad Daffa Ar-Rozy (I0324087)
   
# Pendataan-stok-BBM-di-SPBU
DESKRIPSI PEMROGRAMAN

Pemrograman ini dirancang untuk mendukung pengelolaan stok bahan bakar minyak (BBM) di Stasiun Pengisian Bahan Bakar Umum (SPBU). Sistem ini mencakup pendataan, pemantauan, dan analisis stok BBM, termasuk jenis Pertalite, Pertamax, dan Solar, yang merupakan BBM utama yang digunakan masyarakat. Dengan solusi ini, pengelola SPBU dapat menghindari kekurangan stok, memprediksi kebutuhan pengadaan, dan mengoptimalkan distribusi BBM ke konsumen. Sistem ini cocok digunakan oleh SPBU dari berbagai skala, mulai dari SPBU kecil hingga jaringan SPBU besar, serta memungkinkan integrasi dengan sistem lain seperti platform logistik atau manajemen distribusi BBM.

FITUR UTAMA 
1. Pendataan Stok BBM : Memungkinkan input data stok BBM harian untuk Pertalite, Pertamax, dan Solar.
2. Pemantauan Penjualan BBM : Menghitung volume BBM yang terjual berdasarkan selisih stok awal dan akhir.
3. Notifikasi Stok Rendah : Memberikan peringatan otomatis jika stok salah satu jenis BBM mendekati batas ambang.
4. Manajemen Pengadaan : Mendukung pencatatan jadwal pengiriman ulang BBM dan mencatat histori pengadaan.

ALUR KERJA
1. Input Stok : Operator memasukkan jumlah stok awal saat SPBU mulai beroperasi dan stok akhir setelah operasional selesai.
2. Pemantauan dan Penjualan : Sistem menghitung penjualan harian secara otomatis berdasarkan perbedaan stok awal dan akhir.
3. Notifikasi dan Pengadaan : Jika stok mendekati batas ambang, sistem akan mengirimkan notifikasi agar operator segera menghubungi pemasok untuk melakukan pengisian ulang.
4. Laporan dan Analisis : Operator dapat mengunduh laporan harian atau menganalisis data jangka panjang untuk mengidentifikasi pola konsumsi.

STRUKTUR DATABASE
Bahasa Pemrograman : Python 
KOLOM              TIPE DATA        DESKRIPSI 
id                 Integer          Nomor unik identifikasi entri
jenis_bbm          VARCHAR	        Nama jenis BBM (Pertalite/Pertamax/Solar)
volume_awal        DECIMAL	        Volume stok awal
volume_masuk       DECIMAL          Volume BBM yang masuk
volume_keluar      DECIMAL          Volume BBM yang terjual
volume_akhir       DECIMAL          Volume stok akhir
tanggal_input	     DATE             Tanggal pencatatan stok
petugas_id         Integer          ID petugas yang melakukan pencatatan






