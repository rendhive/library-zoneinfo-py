from zoneinfo import ZoneInfo
import datetime

month = 10
year = 2023
last_day = (datetime.datetime(year, month + 1, 1, tzinfo=ZoneInfo('UTC')) - datetime.timedelta(days=1)).day
print(f"Banyaknya hari di bulan {month}/{year} UTC: {last_day}")
# Fungsi: Menghitung jumlah hari dalam bulan tertentu.
# Kondisi: Ketika Anda perlu memvalidasi dan menghitung tanggal dan bulan.
