from zoneinfo import ZoneInfo
import datetime

now = datetime.datetime.now(ZoneInfo('UTC'))
converted_time = now.astimezone(ZoneInfo('Asia/Tokyo'))
print("Waktu saat ini di Tokyo dari UTC:", converted_time)
# Fungsi: Menampilkan waktu terkonversi ke zona waktu Tokyo dari UTC.
# Kondisi: Ketika Anda perlu melakukan konversi waktu antara dua zona yang berbeda.
