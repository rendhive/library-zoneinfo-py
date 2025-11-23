from zoneinfo import ZoneInfo
import datetime

specific_time = datetime.datetime(2023, 10, 4, 15, 0, tzinfo=ZoneInfo('Europe/Berlin'))
print("Waktu spesifik di Berlin:", specific_time)
# Fungsi: Menciptakan objek waktu spesifik dengan zona waktu terkait.
# Kondisi: Ketika Anda perlu menetapkan objek waktu ke zona waktu tertentu.
