# Menggunakan break untuk menghentikan perulangan
while True:
    n = int(input("Masukkan angka yang bisa dibagi dengan 3: "))
    if n % 3 != 0:
        break
    print("%d bisa dibagi dengan 3" % n)

# Menggunakan continue untuk melanjutkan ke iterasi berikutnya
for i in range(10):
    if i < 3 or i > 7:
        continue
    print(i)

# Menggunakan label perulangan untuk mengontrol perulangan terluar
max_bintang = int(input("Masukkan jumlah maksimal bintang: "))

outer_loop = True
for i in range(max_bintang):
    if not outer_loop:
        break

    for j in range(i + 1):
        print("*", end=" ")
        if j >= 7:
            outer_loop = False
            break
    print()
