from zoneinfo import ZoneInfo
import datetime

# Menggunakan timezone untuk menghitung waktu yang tepat
now = datetime.datetime.now(ZoneInfo('Europe/Paris'))
specific_time = now.replace(hour=9, minute=0)  # Set waktu spesifik
print("Waktu spesifik di Paris:", specific_time)
# Fungsi: Menghitung atau mengatur waktu yang tepat dalam zona waktu tertentu.
# Kondisi: Ketika Anda ingin menetapkan waktu tertentu dalam suatu zona waktu.
