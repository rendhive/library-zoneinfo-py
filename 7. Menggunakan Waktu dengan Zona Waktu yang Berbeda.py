from zoneinfo import ZoneInfo
import datetime

new_york_time = datetime.datetime(2023, 10, 4, 12, 0, tzinfo=ZoneInfo('America/New_York'))
print("Waktu di New York:", new_york_time)
# Fungsi: Menggunakan objek datetime dengan zona waktu spesifik.
# Kondisi: Ketika Anda perlu menetapkan waktu untuk zona waktu khusus.
