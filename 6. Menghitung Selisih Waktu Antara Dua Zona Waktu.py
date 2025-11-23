from zoneinfo import ZoneInfo
import datetime

time_jakarta = datetime.datetime.now(ZoneInfo('Asia/Jakarta'))
time_london = datetime.datetime.now(ZoneInfo('Europe/London'))
difference = time_jakarta - time_london
print(f"Selisih waktu antara Jakarta dan London: {difference}")
# Fungsi: Menghitung selisih waktu antara dua zona waktu.
# Kondisi: Saat Anda perlu mengetahui berapa banyak jam perbedaan antara zona waktu.
