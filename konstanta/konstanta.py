# Deklarasi konstanta di Python dilakukan menggunakan bantuan tipe class bernama typing.Final.
# Untuk menggunakannya, typing.Final perlu di-import terlebih dahulu menggunakan keyword from dan import.
from typing import Final

# Contoh Penggunaan Konstanta
PI: Final = 3.14
print("pi:", PI)

# Tipe Final digunakan untuk menandai suatu variabel sebagai konstanta yang nilainya tidak bisa diubah.
# Cara penerapan Final bisa dengan menuliskan tipe data konstanta secara eksplisit, atau boleh tidak ditentukan (tipe akan diidentifikasi oleh interpreter berdasarkan tipe data nilainya).
TOTAL_MONTH: Final[int] = 12

# Naming convention konstanta
# Menurut dokumentasi PEP 8 – Style Guide for Python Code, nama konstanta harus ditulis dalam huruf besar (UPPER_CASE).
MAX_VALUE: Final = 100

# Definisikan konstanta Pi tanpa tipe clas typing.Final
PI = 3.14159

# Gunakan konstanta Pi untuk menghitung luas lingkaran
radius = 5
luas_lingkaran = PI * (radius ** 2)
print("Luas lingkaran dengan jari-jari 5 adalah:", luas_lingkaran)

