import csv
import os
import re

class ManajemenUser:
    def __init__(self, file_csv='users.csv'):
        self.file_csv = file_csv
        self.users = self.baca_csv()

    def baca_csv(self):
        if not os.path.exists(self.file_csv):
            return {}
        
        users = {}
        with open(self.file_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) == 3:
                    users[row[0]] = {
                        'password': row[1],
                        'foto_profil': row[2]
                    }
        return users

    def validasi_username(self, username):
        return len(username) >= 6

    def validasi_password(self, password):
        return len(password) >= 6

    def tambah_user(self, username, password, foto_profil):
        if not self.validasi_username(username):
            raise ValueError("Username minimal 6 karakter")
        
        if not self.validasi_password(password):
            raise ValueError("Password minimal 6 karakter")
        
        self.users[username] = {
            'password': password,
            'foto_profil': foto_profil
        }
        
        # Simpan ke CSV
        with open(self.file_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Password', 'Foto Profil'])
            for user, data in self.users.items():
                writer.writerow([user, data['password'], data['foto_profil']])
