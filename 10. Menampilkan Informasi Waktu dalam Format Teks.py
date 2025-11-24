from zoneinfo import ZoneInfo
import datetime

now = datetime.datetime.now(ZoneInfo('Australia/Sydney'))
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")
print("Waktu sekarang di Sydney:", formatted_time)
# Fungsi: Menampilkan waktu dalam format strings yang dapat dibaca.
# Kondisi: Ketika Anda perlu memberikan output yang jelas tentang waktu saat ini.
