from zoneinfo import ZoneInfo

zone = ZoneInfo('America/Los_Angeles')
print("Offset dari zona ini:", zone.utcoffset(datetime.datetime.now()))
# Fungsi: Mengetahui offset zona waktu dari zona tertentu.
# Kondisi: Ketika Anda perlu verifikasi offset dari zona waktu untuk kalkulasi lebih lanjut.
