from zoneinfo import ZoneInfo
import datetime

utc_now = datetime.datetime.now(ZoneInfo('UTC'))
print("UTC sekarang:", utc_now)
# Fungsi: Menampilkan waktu UTC saat ini.
# Kondisi: Ketika Anda memerlukan waktu yang konsisten secara internasional.
