from zoneinfo import ZoneInfo
import datetime

time1 = datetime.datetime(2023, 10, 4, 12, 0, tzinfo=ZoneInfo('America/New_York'))
time2 = datetime.datetime(2023, 10, 4, 12, 0, tzinfo=ZoneInfo('Asia/Tokyo'))
if time1 < time2:
    print("Waktu New York kurang dari waktu Tokyo.")
else:
    print("Waktu New York lebih dari atau sama dengan waktu Tokyo.")
# Fungsi: Membandingkan waktu antara dua zona yang berbeda.
# Kondisi: Ketika Anda perlu menganalisis atau mengambil keputusan berdasarkan waktu dari dua lokasi.
