from zoneinfo import ZoneInfo
import datetime

utc_time = datetime.datetime.now(ZoneInfo('UTC'))
jakarta_time = utc_time.astimezone(ZoneInfo('Asia/Jakarta'))
print("Waktu saat ini di Jakarta dari UTC:", jakarta_time)
# Fungsi: Mengonversi waktu dari zona UTC ke zona Jakarta.
# Kondisi: Saat Anda perlu menampilkan waktu yang relevan untuk zona waktu tertentu.
