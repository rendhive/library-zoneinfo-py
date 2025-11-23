from zoneinfo import ZoneInfo
import datetime
import calendar

zone = ZoneInfo('America/New_York')
now = datetime.datetime.now(zone)
print("Kalender bulan sekarang:", calendar.month(now.year, now.month))
# Fungsi: Menampilkan kalender bulan saat ini dengan mempertimbangkan zona waktu.
# Kondisi: Ketika Anda perlu mencetak informasi kalender dengan waktu lokal.
