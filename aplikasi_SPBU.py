import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from datetime import datetime
import os
from PIL import Image, ImageTk
from csv1 import csv1
from user_management import ManajemenUser
from stok_management import StokBBM

class AplikasiSPBU:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pendataan BBM Pertamina")
        self.root.geometry("800x600")
        
        #warna merah
        self.root.configure(bg='#DC241F')  
        
        
        #inisialisasi modul
        self.manajemen_user = ManajemenUser()
        self.stok_bbm = StokBBM()
        
        #data pembelian
        self.pembelian_data = []
        self.current_user = None
        self.foto_profil = None
        
        #login menu
        self.menu_login()

    def menu_login(self):
        self.clear_window()
        
        #background
        self.root.configure(bg='#DC241F')
        
        frame = tk.Frame(self.root, bg='white', padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(frame, text="Login SPBU Pertamina", font=("Arial", 16), fg='#DC241F', bg='white').pack(pady=10)
        
        #username
        tk.Label(frame, text="Username", bg='white').pack(pady=5)
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.pack(pady=5)
        
        #password
        tk.Label(frame, text="Password", bg='white').pack(pady=5)
        self.password_entry = tk.Entry(frame, show='*', width=30)
        self.password_entry.pack(pady=5)
        
        #foto profil
        self.foto_label = tk.Label(frame, text="Belum ada foto profil", bg='white')
        self.foto_label.pack(pady=10)
        
        tk.Button(frame, text="Pilih Foto Profil", command=self.pilih_foto_profil, 
                  bg='#DC241F', fg='white').pack(pady=10)
        
        #tombol login dan daftar
        btn_frame = tk.Frame(frame, bg='white')
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Login", command=self.login, 
                  bg='#DC241F', fg='white', width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Daftar", command=self.daftar, 
                  bg='#DC241F', fg='white', width=15).pack(side=tk.LEFT, padx=5)

    def pilih_foto_profil(self):
        filename = filedialog.askopenfilename(
            title="Pilih Foto Profil", 
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if filename:
            #simpan path foto
            self.foto_profil = filename
            
            #tampilkan preview foto
            try:
                #buka dan resize gambar
                img = Image.open(filename)
                img.thumbnail((100, 100))  # Resize gambar
                photo = ImageTk.PhotoImage(img)
                
                #update label dengan foto
                self.foto_label.config(image=photo, text="")
                self.foto_label.image = photo
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memuat foto: {e}")
                self.foto_label.config(text="Gagal memuat foto", image='')

    def daftar(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        try:
            #pastikan foto profil dipilih
            if not self.foto_profil:
                messagebox.showwarning("Peringatan", "Silakan pilih foto profil")
                return
            
            #tambah user
            self.manajemen_user.tambah_user(username, password, self.foto_profil)
            messagebox.showinfo("Sukses", "Akun berhasil dibuat")
            
            #set current user dan pindah ke menu utama
            self.current_user = username
            self.menu_utama()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        users = self.manajemen_user.users
        if username in users and users[username]['password'] == password:
            #set current user
            self.current_user = username
            
            #set foto profil dari data user
            self.foto_profil = users[username].get('foto_profil', None)
            
            #pindah ke menu utama
            self.menu_utama()
        else:
            messagebox.showerror("Error", "Login gagal")

    def logout(self):
        self.current_user = None
        self.foto_profil = None
        self.menu_login()

    def menu_utama(self):
        self.clear_window()
        
        #header dengan info user
        header_frame = tk.Frame(self.root, bg='#DC241F')
        header_frame.pack(fill='x')
        
        #tampilkan foto profil di header
        if self.foto_profil and os.path.exists(self.foto_profil):
            try:
                img = Image.open(self.foto_profil)
                img.thumbnail((50, 50))  
                photo = ImageTk.PhotoImage(img)
                
                foto_label = tk.Label(header_frame, image=photo, bg='#DC241F')
                foto_label.image = photo  
                foto_label.pack(side='left', padx=10, pady=5)
            except Exception:
                pass
        
        #label nama user
        tk.Label(header_frame, text=f"Selamat Datang, {self.current_user}", 
                 fg='white', bg='#DC241F', font=('Arial', 12)).pack(side='left', padx=10)
        
        #tombol logout
        tk.Button(header_frame, text="Logout", command=self.logout, 
                  bg='white', fg='#DC241F').pack(side='right', padx=10, pady=5)
        
        #menu utama
        tk.Label(self.root, text="Menu Utama SPBU Pertamina", 
                 font=("Arial", 16), fg='#DC241F').pack(pady=20)
        
        #frame untuk menu
        menu_frame = tk.Frame(self.root)
        menu_frame.pack()
        
        #daftar menu
        menus = [
            ("Riwayat Pembelian", self.menu_riwayat),
            ("Input Pembelian", self.menu_pendataan),
            ("Keluar", self.root.quit)
        ]
        
        #tombol menu
        for label, command in menus:
            tk.Button(menu_frame, text=label, command=command, 
                      bg='#DC241F', fg='white', width=20, height=2).pack(pady=10)

    def menu_riwayat(self):
        self.clear_window()
        
        tk.Label(self.root, text="Riwayat Pembelian", 
                 font=("Arial", 16), fg='#DC241F').pack(pady=10)
        
        #tabel riwayat pembelian
        columns = ("Jenis BBM", "Jumlah (Liter)", "Harga per Liter", "Total Harga", "Sisa Stok")
        tree = ttk.Treeview(self.root, columns=columns, show='headings')
        
        #atur kolom
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')
        
        tree.pack(pady=10, padx=20, fill='both', expand=True)
        
        #tambahkan data pembelian ke tabel
        for data in self.pembelian_data:
            tree.insert("", "end", values=data)
        
        #tombol kembali
        tk.Button(self.root, text="Kembali", command=self.menu_utama, 
                  bg='#DC241F', fg='white').pack(pady=10)

    def menu_pendataan(self):
        self.clear_window()
        
        tk.Label(self.root, text="Input Pembelian BBM", 
                 font=("Arial", 16), fg='#DC241F').pack(pady=10)
        
        #tampilkan stok saat ini
        stok_frame = tk.Frame(self.root)
        stok_frame.pack(pady=10)
        
        for jenis, stok in self.stok_bbm.stok.items():
            tk.Label(stok_frame, text=f"Stok {jenis}: {stok} Liter", 
                     fg='#DC241F').pack(side=tk.LEFT, padx=10)
        
        #frame input
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        #pilih jenis BBM
        jenis_bbm = tk.StringVar(value="Pertalite")
        tk.Label(input_frame, text="Jenis BBM:", fg='#DC241F').grid(row=0, column=0, padx=5)
        jenis_options = ["Pertalite", "Pertamax", "Solar"]
        jenis_dropdown = ttk.Combobox(input_frame, textvariable=jenis_bbm, 
                                      values=jenis_options, state="readonly")
        jenis_dropdown.grid(row=0, column=1, padx=5)
        
        #tanggal
        tk.Label(input_frame, text="Tanggal (dd,mm,yyyy):", fg='#DC241F').grid(row=1, column=0, padx=5)
        tanggal_entry = tk.Entry(input_frame)
        tanggal_entry.grid(row=1, column=1, padx=5)
        
        #metode pembelian
        tk.Label(input_frame, text="Metode:", fg='#DC241F').grid(row=2, column=0, padx=5)
        metode_var = tk.StringVar(value="Liter")
        metode_dropdown = ttk.Combobox(input_frame, textvariable=metode_var, 
                                       values=["Liter", "Rupiah"], state="readonly")
        metode_dropdown.grid(row=2, column=1, padx=5)
        
        #input jumlah
        tk.Label(input_frame, text="Jumlah:", fg='#DC241F').grid(row=3, column=0, padx=5)
        input_entry = tk.Entry(input_frame)
        input_entry.grid(row=3, column=1, padx=5)
        
        def proses_pembelian():
            try:
                jenis = jenis_bbm.get()
                metode = metode_var.get()
                jumlah_input = float(input_entry.get())
                
                #validasi tanggal
                tanggal_str = tanggal_entry.get()
                tanggal_parts = tanggal_str.split(',')
                tanggal = datetime(
                    day=int(tanggal_parts[0]), 
                    month=int(tanggal_parts[1]), 
                    year=int(tanggal_parts[2])
                )
                
                #hitung jumlah liter dan total harga
                total_harga = self.stok_bbm.hitung_total_pembelian(jenis, jumlah_input, metode)
                
                #cek dan kurangi stok
                if self.stok_bbm.kurangi_stok(jenis, jumlah_input):
                    #catat pembelian
                    data_pembelian = (
                        jenis, 
                        jumlah_input, 
                        self.stok_bbm.harga[jenis], 
                        total_harga, 
                        self.stok_bbm.cek_stok(jenis)
                    )
                    self.pembelian_data.append(data_pembelian)
                    
                    messagebox.showinfo("Sukses", f"Pembelian {jenis} berhasil")
                    
                    #cek restok otomatis
                    if self.stok_bbm.restok_otomatis(jenis):
                        messagebox.showinfo("Restok", f"Stok {jenis} telah direstok")
                else:
                    messagebox.showerror("Error", "Stok tidak mencukupi")
            
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        #tombol proses
        proses_btn = tk.Button(self.root, text="Proses Pembelian", 
                               command=proses_pembelian, 
                               bg='#DC241F', fg='white')
        proses_btn.pack(pady=10)
        
        #tombol kembali
        tk.Button(self.root, text="Kembali", command=self.menu_utama, 
                  bg='#DC241F', fg='white').pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = AplikasiSPBU(root)
    root.mainloop()

if __name__ == "__main__":
    main()
