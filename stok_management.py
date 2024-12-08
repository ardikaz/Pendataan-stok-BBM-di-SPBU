from datetime import datetime, timedelta

class StokBBM:
    def __init__(self):
        self.stok = {
            'Pertalite': 1000,
            'Pertamax': 1000,
            'Solar': 1000
        }
        self.harga = {
            'Pertalite': 10000,
            'Pertamax': 14000,
            'Solar': 9000
        }
        self.ambang_batas = 200  # Ambang batas stok
        self.riwayat_restok = []
        self.terakhir_restok = {}

    def cek_stok(self, jenis_bbm):
        return self.stok[jenis_bbm]

    def kurangi_stok(self, jenis_bbm, jumlah):
        if self.stok[jenis_bbm] >= jumlah:
            self.stok[jenis_bbm] -= jumlah
            return True
        return False

    def restok_otomatis(self, jenis_bbm):
        # Cek apakah stok di bawah ambang batas
        if self.stok[jenis_bbm] < self.ambang_batas:
            # Cek apakah sudah 3 hari sejak restok terakhir
            terakhir = self.terakhir_restok.get(jenis_bbm)
            sekarang = datetime.now()
            
            if terakhir is None or (sekarang - terakhir).days >= 3:
                # Restok
                jumlah_restok = 1000 - self.stok[jenis_bbm]
                self.stok[jenis_bbm] = 1000
                
                # Catat riwayat restok
                self.riwayat_restok.append({
                    'jenis_bbm': jenis_bbm,
                    'tanggal': sekarang.strftime("%Y-%m-%d"),
                    'jumlah': jumlah_restok
                })
                
                # Update waktu restok terakhir
                self.terakhir_restok[jenis_bbm] = sekarang
                
                return True
        return False

    def hitung_total_pembelian(self, jenis_bbm, jumlah, metode='Liter'):
        # Hitung total harga berdasarkan metode pembelian
        if metode == 'Liter':
            return jumlah * self.harga[jenis_bbm]
        elif metode == 'Rupiah':
            return jumlah / self.harga[jenis_bbm]
