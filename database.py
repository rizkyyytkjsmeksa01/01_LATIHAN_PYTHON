import os
from datetime import datetime
from getpass import getpass

import gspread
from google.oauth2.service_account import Credentials

# Scope akses Google API
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Lokasi file credentials.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")

# Autentikasi
creds = Credentials.from_service_account_file(
    CREDENTIALS_FILE,
    scopes=SCOPES
)

client = gspread.authorize(creds)

# Buka Google Spreadsheet
worksheet = client.open_by_key(
    "1N85CB39u3U9E84-P7o2FqEFWc3K0YKUrzntEVxYQeRI"
).sheet1

# Buat header jika spreadsheet masih kosong
if not worksheet.cell(1, 1).value:
    worksheet.append_row(["Username", "Kode", "Waktu"])

# Input data
username = input("Masukkan Username : ")
kode = getpass("Masukkan Kode : ")

# Ambil waktu saat ini
waktu = datetime.now().strftime("%H:%M:%S")

# Simpan ke Google Sheets
worksheet.append_row([username, kode, waktu])

# Output
print("\n======================")
print("DATA BERHASIL DISIMPAN")
print("======================")
print(f"Username : {username}")
print("Kode     : ******")
print(f"Waktu    : {waktu}")