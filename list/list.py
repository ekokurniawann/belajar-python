# Pengenalan list
list_1 = [10, 70, 20]  # List dengan elemen integer
list_2 = [  # List multi-baris dengan elemen string
    'ab',
    'cd',
    'hi',
    'ca'
]
list_3 = [3.14, 'hello python', True, False]  # List dengan elemen berbagai tipe data
list_4 = []  # List kosong

# Perulangan list menggunakan nilai element dan index
for e in list_1:
    print("elem:", e)

for i in range(len(list_1)):
    print("index:", i, "elem:", list_1[i])

for i, v in enumerate(list_1):
    print("index:", i, "elem:", v)

# Nested list
matrix = [  # List sebagai matriks
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]

for row in matrix:
    for cell in row:
        print(cell, end=" ")  # Mencetak elemen dalam satu baris
    print()  # Pindah baris setiap satu baris selesai

# Fungsi list()
range_1 = range(10)  # Membuat range dari 0 sampai 9
list_1 = list(range_1)  # Mengonversi range menjadi list
print(list_1)

range_2 = range(0, 22, 3)  # Membuat range dari 0 sampai 21 dengan interval 3
list_2 = list(range_2)
print(list_2)

range_3 = range(100, 0, -10)  # Membuat range dari 100 sampai 10 dengan interval -10
list_3 = list(range_3)
print(list_3)

alphabets = list('abcdefgh')  # Mengonversi string menjadi list dengan setiap karakter sebagai elemen
print(alphabets)

tuple_1 = (1, 2, 3, 4)
numbers = list(tuple_1)  # Mengonversi tuple menjadi list
print(numbers)

# Operasi pada list
list_1 = [10, 70, 20]

elem_1st = list_1[0]  # Mengakses elemen pertama
elem_2nd = list_1[1]  # Mengakses elemen kedua
elem_3rd = list_1[2]  # Mengakses elemen ketiga

print(elem_1st, elem_2nd, elem_3rd)

n = 70
if n in list_1:  # Mengecek apakah nilai 70 ada dalam list
    print(n, "is exists")
else:
    print(n, "is NOT exists")

list_2 = ['ab', 'cd', 'hi', 'ca']
print('list_2:', list_2)

slice_1 = list_2[1:3]  # Mengambil slice dari indeks 1 hingga 2
print('slice_1:', slice_1)

list_2[1] = 'zk'  # Mengubah elemen indeks 1
list_2[2] = 'sa'  # Mengubah elemen indeks 2
print('after: ', list_2)

list_1 = [10, 70, 20]
print('before: ', list_1)

list_1.append(88)  # Menambahkan elemen ke list
list_1.append(87)
print('after: ', list_1)

list_1 = [10, 70, 20]
print('before: ', list_1)

list_1.extend([88, 77])  # Menambahkan elemen dari list lain ke list
print('after: ', list_1)

list_1 = [10, 70, 20]
print('before: ', list_1)

list_1[len(list_1):] = [88, 87]  # Menambahkan elemen dari list lain menggunakan slicing
print('after: ', list_1)

list_3 = [10, 70, 20, 70]

list_3.insert(0, 15)  # Menyisipkan elemen di indeks 0
print(list_3)

list_3.insert(2, 25)  # Menyisipkan elemen di indeks 2
print(list_3)

list_3 = [10, 70, 20, 70]

list_3.remove(70)  # Menghapus elemen pertama dengan nilai 70
print(list_3)

list_3.remove(70)  # Menghapus elemen pertama dengan nilai 70
print(list_3)

list_3 = [10, 70, 20, 70]

x = list_3.pop(2)  # Menghapus elemen di indeks 2
print('list_3:', list_3)
print('removed element:', x)

x = list_3.pop()  # Menghapus elemen terakhir
print('list_3:', list_3)
print('removed element:', x)

list_3 = [10, 70, 20, 70]
print('len:', len(list_3), "data:", list_3)

del list_3[1]  # Menghapus elemen di indeks 1
print('len:', len(list_3), "data:", list_3)

list_3 = [10, 70, 20, 70]

del list_3[1:3]  # Menghapus elemen dari indeks 1 hingga 2
print(list_3)

list_3 = [10, 70, 20, 70]
total = len(list_3)  # Menghitung jumlah elemen dalam list
print(total)

list_3 = [10, 70, 20, 70]
count = list_3.count(70)  # Menghitung berapa kali nilai 70 muncul dalam list
print('jumlah element dengan data `70`:', count)

list_2 = ['ab', 'cd', 'hi', 'ca']

idx_1st = list_2.index('cd')  # Mencari indeks dari nilai 'cd'
print('idx_1st: ', idx_1st)

# Mengosongkan list
list_1 = [10, 70, 20]
list_1.clear()  # Mengosongkan list
print(list_1)

list_1 = [10, 70, 20]
list_1 = []  # Mengosongkan list
print(list_1)

list_1 = [10, 70, 20]
del list_1[:]  # Mengosongkan list
print(list_1)

# Membalik urutan element list
list_1 = [10, 70, 20]
list_1.reverse()  # Membalik urutan elemen dalam list
print(list_1)

# Copy list
list_1 = [10, 70, 20]
list_2 = list_1.copy()  # Menyalin isi list ke list lain
print(list_1)
print(list_2)

list_1 = [10, 70, 20]
list_2 = list_1[:]  # Menyalin isi list ke list lain
print(list_1)
print(list_2)

# Sorting
list_1 = [10, 70, 20]
list_1.sort()  # Mengurutkan elemen list secara ascending
print(list_1)

list_2 = ['z', 'h', 'c']
list_2.sort()  # Mengurutkan elemen list secara alfabetik
print(list_2)
