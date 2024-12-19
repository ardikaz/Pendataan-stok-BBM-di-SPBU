import csv
import os

class CSVManager:
    def __init__(self, user_file='users.csv', transaction_file='transactions.csv'):
        self.user_file = user_file
        self.transaction_file = transaction_file

        # Buat file jika belum ada
        self._initialize_file(self.user_file, ['Username', 'Password', 'Foto Profil'])
        self._initialize_file(self.transaction_file, ['Username', 'Jenis BBM', 'Jumlah (Liter)', 'Harga per Liter', 'Total Harga', 'Tanggal'])

    def _initialize_file(self, file_name, headers):
        if not os.path.exists(file_name):
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

    def save_user(self, username, password, foto_profil):
        """Menyimpan data pengguna baru."""
        with open(self.user_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, foto_profil])

    def save_transaction(self, username, jenis_bbm, jumlah, harga_per_liter, total_harga, tanggal):
        """Menyimpan data transaksi."""
        with open(self.transaction_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([username, jenis_bbm, jumlah, harga_per_liter, total_harga, tanggal])

    def load_users(self):
        """Memuat data pengguna dari file CSV."""
        users = {}
        with open(self.user_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users[row['Username']] = {
                    'password': row['Password'],
                    'foto_profil': row['Foto Profil']
                }
        return users

    def load_transactions(self):
        """Memuat data transaksi dari file CSV."""
        transactions = []
        with open(self.transaction_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
        return transactions