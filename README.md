# library-zoneinfo-py
# Penggunaan Modul `zoneinfo` di Python

## Deskripsi
Modul `zoneinfo` yang diperkenalkan di Python 3.9 menyediakan cara yang efisien untuk menangani zona waktu, memungkinkan pengembang untuk bekerja dengan waktu dan tanggal secara global dengan memperhitungkan perbedaan waktu antar zona.

## Daftar Isi
- [Instalasi](#instalasi)
- [Penggunaan Dasar](#penggunaan-dasar)
  - [Mendapatkan Waktu Saat Ini dalam Zona Waktu Tertentu](#mendapatkan-waktu-saat-ini-dalam-zona-waktu-tertentu)
  - [Mengubah Waktu ke Zona Waktu Lain](#mengubah-waktu-ke-zona-waktu-lain)
  - [Menampilkan Daftar Zona Waktu Tersedia](#menampilkan-daftar-zona-waktu-teravailable)
  - [Menghitung Selisih Waktu Antara Dua Zona Waktu](#menghitung-selisih-waktu-antara-dua-zona-waktu)
  - [Menampilkan Waktu UTC Saat Ini](#menampilkan-waktu-utc-saat-ini)
- [Kondisi Penggunaan](#kondisi-penggunaan)
- [Referensi](#referensi)

## Instalasi
Modul `zoneinfo` sudah termasuk dalam pustaka standar Python (mulai dari versi 3.9). Pastikan Anda telah menggunakan versi Python 3.9 atau lebih baru. Tidak perlu menginstal modul ini secara terpisah.

## Penggunaan Dasar

### Mendapatkan Waktu Saat Ini dalam Zona Waktu Tertentu
Untuk mendapatkan waktu saat ini dalam zona waktu tertentu, Anda dapat menggunakan kode berikut:

```python
from zoneinfo import ZoneInfo
import datetime

now = datetime.datetime.now(ZoneInfo('Asia/Jakarta'))
print("Waktu sekarang di Jakarta:", now)
```

### Mengubah Waktu ke Zona Waktu Lain
Anda dapat mengubah waktu dari satu zona ke zona lain. Contoh:

```python
from zoneinfo import ZoneInfo
import datetime

utc_time = datetime.datetime.now(ZoneInfo('UTC'))
jakarta_time = utc_time.astimezone(ZoneInfo('Asia/Jakarta'))
print("Waktu saat ini di Jakarta dari UTC:", jakarta_time)
```

### Menampilkan Daftar Zona Waktu Tersedia
Untuk menampilkan semua zona waktu yang tersedia, gunakan kode berikut:

```python
import zoneinfo

print("Zona waktu yang tersedia:")
for tz in zoneinfo.available_timezones():
    print(tz)
```

### Menghitung Selisih Waktu Antara Dua Zona Waktu
Anda bisa menghitung selisih waktu antara dua lokasi, contohnya:

```python
from zoneinfo import ZoneInfo
import datetime

time_jakarta = datetime.datetime.now(ZoneInfo('Asia/Jakarta'))
time_london = datetime.datetime.now(ZoneInfo('Europe/London'))
difference = time_jakarta - time_london
print(f"Selisih waktu antara Jakarta dan London: {difference}")
```

### Menampilkan Waktu UTC Saat Ini
Untuk mendapatkan waktu UTC saat ini, Anda bisa menggunakan:

```python
from zoneinfo import ZoneInfo
import datetime

utc_now = datetime.datetime.now(ZoneInfo('UTC'))
print("UTC sekarang:", utc_now)
```

## Kondisi Penggunaan
- **Pengelolaan Waktu Global**: Ketika Anda perlu menampilkan atau menghitung waktu dari berbagai zona waktu di seluruh dunia.
- **Aplikasi Internasional**: Untuk aplikasi yang melayani pengguna dari zona waktu yang berbeda.
- **Koordinasi Waktu**: Ketika Anda perlu membandingkan atau menghitung waktu berdasarkan perbedaan waktu.

## Referensi
- [Dokumentasi Resmi Python: zoneinfo](https://docs.python.org/3/library/zoneinfo.html)

Dengan menggunakan modul `zoneinfo`, Anda dapat dengan mudah menangani dan memanipulasi waktu dalam aplikasi Python Anda dengan memikirkan perbedaan waktu secara global!

