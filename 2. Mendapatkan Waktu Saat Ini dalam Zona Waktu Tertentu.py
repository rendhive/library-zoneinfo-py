from zoneinfo import ZoneInfo
import datetime

now = datetime.datetime.now(ZoneInfo('Asia/Jakarta'))
print("Waktu sekarang di Jakarta:", now)
# Fungsi: Mendapatkan waktu saat ini dalam zona waktu Jakarta.
# Kondisi: Ketika Anda perlu menampilkan waktu berdasarkan zona waktu lokal tertentu.
