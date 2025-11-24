from zoneinfo import ZoneInfo
import time

zone = ZoneInfo('Pacific/Auckland')
start_time = datetime.datetime.now(zone)

# Simulasi kegiatan berlangsung
time.sleep(2)  # Simulasi waktu tunggu 2 detik

end_time = datetime.datetime.now(zone)
duration = end_time - start_time
print("Waktu kegiatan:", duration)
# Fungsi: Mengukur durasi dari suatu kegiatan yang dilakukan.
# Kondisi: Ketika Anda perlu tahu berapa lama waktu yang terpakai untuk suatu aktivitas.
