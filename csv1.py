import csv
import os

class csv1:
    def simpan_username(username, filename='usernames.csv'):
    # Cek apakah file CSV sudah ada
        file_exists = os.path.isfile(filename)

    # Buka file CSV dalam mode append
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)

        # Jika file baru, tulis header
            if not file_exists:
                writer.writerow(['Username'])  # Menulis header

        # Tulis username ke file
            writer.writerow([username])
            print(f"Username '{username}' berhasil disimpan ke {filename}.")

    def main():
    # Minta input username dari pengguna
        username = input("Masukkan username yang ingin disimpan: ")
