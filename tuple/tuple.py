# Pengenalan Tuple
tuple_1 = (2, 3, 4, "hello python", False)

print("Data tuple_1:", tuple_1)
print("Jumlah elemen tuple_1:", len(tuple_1))

# Mengakses elemen tuple via index
tuple_2 = (2, 3, 4, 5)

print("Elemen dengan indeks 0:", tuple_2[0])
print("Elemen dengan indeks 1:", tuple_2[1])

# Perulangan tuple
tuple_3 = ('ultra instinc shaggy', 'nightwing', 'noob saibot')

print("Elemen tuple_3:")
for character in tuple_3:
    print(character)

# Menggunakan fungsi enumerate()
tuple_4 = ('ultra instinc shaggy', 'nightwing', 'noob saibot')

print("Elemen tuple_4 dengan indeks:")
for index, character in enumerate(tuple_4):
    print("Index:", index, "Elemen:", character)

# Mengecek keberadaan elemen dalam tuple
tuple_5 = (10, 70, 20)
n = 70

if n in tuple_5:
    print(n, "ada dalam tuple_5")
else:
    print(n, "tidak ada dalam tuple_5")

# Nested tuple
tuple_nested = (
    (0, 2),
    (0, 3),
    (2, 2),
    (2, 4)
)

print("Elemen tuple_nested:")
for row in tuple_nested:
    for cell in row:
        print(cell, end=" ")
    print()

# Tuple dalam list
data = [
    ("ultra instinc shaggy", 1, True, ['detective', 'saiyan']),
    ("nightwing", 3, True, ['teen titans', 'bat family']),
    ("noob saibot", 6, False, ['brotherhood of shadow']),
    ("tifa lockhart", 2, True, ['avalanche'])
]

print("Data:")
print("Nama | Peringkat | Menang | Afiliasi")
print("------------------------------------")
for item in data:
    for detail in item:
        print(detail, end=" | ")
    print()

# Fungsi tuple()
# Konversi string ke tuple
alphabets = tuple('abcdefgh')
print("Tuple alphabets:", alphabets)

# Konversi list ke tuple
numbers = tuple([2, 3, 4, 5])
print("Tuple numbers:", numbers)

# Konversi range ke tuple
r = range(0, 3)
rtuple = tuple(r)
print("Tuple dari range:", rtuple)

# Tuple packing dan unpacking
# Tuple packing
first_name = "aerith gainsborough"
rank = 11
win = False

row_data = (first_name, rank, win)

print("Tuple row_data:", row_data)

# Tuple unpacking
student_data = ('aerith gainsborough', 11, False)
student_name, student_rank, student_win = student_data

print("Nama:", student_name)
print("Peringkat:", student_rank)
print("Menang:", student_win)

# Tuple kosong
empty_tuple = ()
print("Tuple kosong:", empty_tuple)

# Operasi pada Tuple
# Concatenation (penggabungan)
tuple_a = (1, 2, 3)
tuple_b = ('a', 'b', 'c')
concatenated_tuple = tuple_a + tuple_b
print("Tuple hasil penggabungan:", concatenated_tuple)

# Repetition (pengulangan)
repeated_tuple = tuple_a * 3
print("Tuple hasil pengulangan:", repeated_tuple)

# Slicing (irisan)
tuple_c = (1, 2, 3, 4, 5)
sliced_tuple = tuple_c[1:4]
print("Tuple hasil irisan:", sliced_tuple)

# Immutability of Tuples
# Coba mengubah nilai pada tuple (akan menghasilkan error)
# tuple_immutable = (1, 2, 3)
# tuple_immutable[0] = 4

# Keuntungan Penggunaan Tuple
# Kecepatan akses data
import timeit

list_time = timeit.timeit(stmt="x[999]", setup="x = list(range(1000))", number=100000)
tuple_time = timeit.timeit(stmt="x[999]", setup="x = tuple(range(1000))", number=100000)

print("Waktu akses data untuk list:", list_time)
print("Waktu akses data untuk tuple:", tuple_time)

# Menggunakan Tuple Sebagai Kunci pada Dictionary
student_records = {
    ('John', 'Doe'): 85,
    ('Jane', 'Smith'): 90,
    ('Bob', 'Johnson'): 80
}

# Tuple dalam Fungsi
def get_student_details():
    name = "John"
    age = 20
    grade = "A"
    return name, age, grade

student_name, student_age, student_grade = get_student_details()
print("Nama Mahasiswa:", student_name)
print("Umur Mahasiswa:", student_age)
print("Grade Mahasiswa:", student_grade)

# Penggunaan Tuple sebagai Parameter Fungsi
# Tuple dapat digunakan sebagai parameter fungsi untuk mengirimkan sejumlah nilai yang berbeda sebagai satu parameter.
def calculate_average(*numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

average = calculate_average(10, 20, 30, 40, 50)
print("Rata-rata:", average)

# Menggabungkan Tuple dengan * Operator
# Operator * digunakan untuk menggabungkan dua tuple.
tuple_1 = (1, 2, 3)
tuple_2 = ('a', 'b', 'c')

combined_tuple = (*tuple_1, *tuple_2)
print("Gabungan Tuple:", combined_tuple)

# Menggunakan Tuple dalam Set
# Tuple dapat digunakan dalam set karena bersifat immutable.
set_of_tuples = {('a', 'b'), ('c', 'd'), ('e', 'f')}
print("Set of Tuples:", set_of_tuples)

# Konversi Tuple ke List dan Sebaliknya
# Tuple dapat dikonversi ke list dan sebaliknya.
tuple_to_list = tuple([1, 2, 3, 4, 5])
print("Tuple to List:", tuple_to_list)
