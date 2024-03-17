# Contoh penggunaan while dengan kontrol nilai boolean
should_continue = True

while should_continue:
    n = int(input("Masukkan angka genap lebih dari 0: "))

    if n <= 0 or n % 2 == 1:
        print(n, "bukan angka genap lebih dari 0")
        should_continue = False
    else:
        print("Angka:", n)

# Contoh perulangan while dengan operasi logika
n = int(input("Masukkan jumlah data maksimal: "))
i = 0

while i < n:
    print("Angka", i)
    i += 1

# Contoh perulangan bercabang (nested while)
n = int(input("Masukkan jumlah data maksimal: "))
i = 0

while i < n:
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1

    print()
    i += 1

# Kombinasi while dan for
n = int(input("Masukkan jumlah data maksimal: "))

for i in range(n):
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1

    print()
