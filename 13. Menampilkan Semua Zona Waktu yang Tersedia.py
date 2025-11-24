import zoneinfo

print("Zona waktu yang tersedia:")
for tz in zoneinfo.available_timezones():
    print(tz)
# Fungsi: Menampilkan daftar semua zona waktu yang tersedia di Python.
# Kondisi: Ketika Anda perlu tahu zona waktu yang dapat Anda gunakan.
