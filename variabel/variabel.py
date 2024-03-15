# Variabel adalah penampung nilai/data yang disimpan di memori komputer
# Di python, variabel dideklrasikan dengan cara yang sederhana
nama = "noval"
hobi = "makan"
umur = 18
laki = True

# Menampilkan nilai variabel
# Gunakan fungsi print() untuk menampilkan nilai variabel
print("===biodata===")
print("nama : %s" % (nama))
print("hobi: %s, umur: %d, laki: %r" % (hobi, umur, laki))

# Nama variabel dianjurkan menggunakan snake_case
pesan = 'halo, selamat pagi'
nilai_ujian = 99.2


# Deklrasi variabel beserta tipe data
# Tipe data variabel bisa ditentukan secara eksplisit
nama: str = "noval"
umur: int = 18
nilai_ujian: float = 99.2

# Mengganti Nilai Variabel
# Nilai variabel dapat diubah kapan saja selama program berjalan.
umur = 22

# Deklarasi Banyak Variabel Sebaris
# Banyak variabel dapat dideklarasikan dalam satu baris.
nilai1, nilai2, nilai3, nilai4 = 24, 25, 26, 21
nilai_rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4

print("rata-rata nilai: %f" % (nilai_rata_rata))

# Menggunakan Variabel dalam Ekspresi
# Variabel dapat digunakan dalam berbagai operasi matematika atau string.
panjang = 10
lebar = 5
luas = panjang * lebar

print(luas)

# Variabel sebagai Argument dalam Fungsi
# Variabel dapat digunakan sebagai argumen saat memanggil fungsi.
def sapa(nama):
    print("Halo,", nama)

sapa("Baswedan")

# Penghapusan Variabel
# Variabel dapat dihapus dari memori menggunakan perintah del.
del nilai1, nilai2, nilai3, nilai4

# Menggabungkan Variabel dengan String
# Variabel dapat digabungkan dengan string menggunakan operator konkatenasi (+) atau formatted string.
nama_depan = "John"
nama_belakang = "Doe"
nama_lengkap = nama_depan + " " + nama_belakang
print("Nama lengkap:", nama_lengkap)

# Variabel Global dan Lokal
# Variabel global dideklarasikan di luar fungsi dan dapat diakses di seluruh program.
# Variabel lokal dideklarasikan di dalam fungsi dan hanya dapat diakses di dalam fungsi tersebut.
variabel_global = 10

def fungsi():
    variabel_lokal = 5
    print("Variabel global:", variabel_global)
    print("Variabel lokal:", variabel_lokal)

fungsi()




