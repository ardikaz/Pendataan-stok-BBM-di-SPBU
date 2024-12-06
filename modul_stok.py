def stok(self):
    self.stok_awal = {
            "Pertalite": 1000,
            "Pertamax": 1000,
            "Solar": 1000
        }
    self.ambang_batas = 200  # Ambang batas stok

def input_stok_awal(self, jenis_bbm, stok):
        self.stok_awal[jenis_bbm] = stok

def cek_stok(self, jenis_bbm):
        return self.stok_awal.get(jenis_bbm, 0)

def restok(self, jenis_bbm):
    if self.cek_stok(jenis_bbm) < self.ambang_batas:
        print('Warning', f'Pembelian mencapai ambang batas')
        self.stok_awal[jenis_bbm] = 1000  # Mengembalikan ke stok awal
        print(f"Stok {jenis_bbm} telah direstok ke {self.stok_awal[jenis_bbm]}.")

def simpan_data(self):
        # Simpan data ke file atau database (opsional)
    pass