import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime # Mengimpor modul fungsi

class AplikasiSPBU:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pendataan Stok BBM SPBU")
        self.root.geometry("600x400")  # Ukuran awal jendela
        self.user_data = {}  # Simpan data pengguna
        self.current_user = None
        self.pembelian_data = []  # Simpan data pembelian

        self.menu_login()

    def menu_login(self):
        self.clear_window()
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Daftar", command=self.daftar).pack(pady=5)

    def daftar(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in self.user_data:
            messagebox.showerror("Error", "Username sudah terdaftar.")
        else:
            self.user_data[username] = password
            messagebox.showinfo("Success", "Akun berhasil dibuat.")
            self.current_user = username
            self.menu_utama()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in self.user_data and self.user_data[username] == password:
            self.current_user = username
            self.menu_utama()
        else:
            messagebox.showerror("Error", "Akun belum terdaftar. Silakan daftar terlebih dahulu.")

    def menu_utama(self):
        self.clear_window()
        tk.Label(self.root, text="Menu Utama", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Lihat Data Riwayat Pembelian dan Restok", command=self.menu_riwayat).pack(pady=10)
        tk.Button(self.root, text="Pendataan Pembelian dan Restok", command=self.menu_pendataan).pack(pady=10)
        tk.Button(self.root, text="Keluar", command=self.root.quit).pack(pady=10)

    def menu_riwayat(self):
        self.clear_window()
        tk.Label(self.root, text="Riwayat Pembelian dan Restok", font=("Arial", 16)).pack(pady=10)
        self.tree = ttk.Treeview(self.root, columns=("Jenis BBM", "Tanggal", "Jumlah (Liter)"), show='headings')
        self.tree.heading("Jenis BBM", text="Jenis BBM")
        self.tree.heading("Tanggal", text="Tanggal")
        self.tree.heading("Jumlah (Liter)", text="Jumlah (Liter)")
        self.tree.pack(pady=10)

        for data in self.pembelian_data:
            self.tree.insert("", "end", values=data)

        tk.Button(self.root, text="Kembali", command=self.menu_utama).pack(pady=10)

    def menu_pendataan(self):
        self.clear_window()
        tk.Label(self.root, text="Pendataan Pembelian dan Restok", font=("Arial", 16)).pack(pady=10)
        self.jenis_bbm = tk.StringVar()
        tk.Radiobutton(self.root, text="Pertalite", variable=self.jenis_bbm, value="Pertalite").pack(pady=5)
        tk.Radiobutton(self.root, text="Pertamax", variable=self.jenis_bbm, value="Pertamax").pack(pady=5)
        tk.Radiobutton(self.root, text="Solar", variable=self.jenis_bbm, value="Solar").pack(pady=5)

        tk.Label(self.root, text="Tanggal Pembelian (dd, mm, yyyy)").pack(pady=5)
        self.tanggal_entry = tk.Entry(self.root)
        self.tanggal_entry.pack(pady=5)
        
        tk.Label(self.root, text="Jumlah Pembelian (Liter)").pack(pady=5)
        self.jumlah_entry = tk.Entry(self.root)
        self.jumlah_entry.pack(pady=5)

        tk.Button(self.root, text="Input Pembelian", command=self.input_pembelian).pack(pady=10)
        tk.Button(self.root, text="Kembali", command=self.menu_utama).pack(pady=5)

    def input_pembelian(self):
        jenis_bbm = self.jenis_bbm.get()
        tanggal_input = self.tanggal_entry.get()
        jumlah_pembelian_input = self.jumlah_entry.get()

        try:
            # Validasi tanggal
            tanggal_parts = tanggal_input.split(',')
            if len(tanggal_parts) != 3:
                raise ValueError("Format tanggal salah. Gunakan format dd, mm, yyyy.")
            tanggal = int(tanggal_parts[0].strip())
            bulan = int(tanggal_parts[1].strip())
            tahun = int(tanggal_parts[2].strip())
            tanggal_pembelian = datetime(year=tahun, month=bulan, day=tanggal)

            # Validasi jumlah pembelian
            jumlah_pembelian = float(jumlah_pembelian_input)
            if jumlah_pembelian > 1000:
                messagebox.showinfo('Warning', f'Pembelian mencapai ambang batas')
            else:
                self.pembelian_data.append((jenis_bbm, tanggal_pembelian.strftime("%Y-%m-%d"), jumlah_pembelian))
                messagebox.showinfo("Success", f"Pembelian {jenis_bbm} pada {tanggal_pembelian.strftime('%Y-%m-%d')} berhasil dicatat.")

            # Update stok
            def restok(self, jenis_bbm):
              if self.cek_stok(jenis_bbm) < self.ambang_batas:
                messagebox.showinfo('Warning', f'Pembelian mencapai ambang batas')
            self.stok_awal[jenis_bbm] = 1000  # Mengembalikan ke stok awal
            print(f"Stok {jenis_bbm} telah direstok ke {self.stok_awal[jenis_bbm]}.")

            self.stok_bbm.input_stok_awal(jenis_bbm, self.stok_bbm.cek_stok(jenis_bbm) - jumlah_pembelian)
            messagebox.showinfo
            

            # Cek stok dan restok jika perlu
            self.stok_bbm.restok(restok)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Fungsi untuk membersihkan jendela
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiSPBU(root)
    root.mainloop()
    