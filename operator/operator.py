# Operator aritmatika
# Penambahan
num = 2 + 2
print("2 + 2 =", num)  # Output: 2 + 2 = 4

# Unary positif
num = +2
print("+2 =", num)  # Output: +2 = 2

# Pengurangan
num = 3 - 2
print("3 - 2 =", num)  # Output: 3 - 2 = 1

# Unary negatif
num = -2
print("-2 =", num)  # Output: -2 = -2

# Perkalian
num = 3 * 3
print("3 * 3 =", num)  # Output: 3 * 3 = 9

# Pembagian
num = 8 / 2
print("8 / 2 =", num)  # Output: 8 / 2 = 4.0

# Pembagian dengan pembulatan ke bawah
num = 10 // 3
print("10 // 3 =", num)  # Output: 10 // 3 = 3

# Modulo (sisa hasil bagi)
num = 7 % 4
print("7 % 4 =", num)  # Output: 7 % 4 = 3

# Pangkat
num = 3 ** 2
print("3 ** 2 =", num)  # Output: 3 ** 2 = 9


# Operator assignment
num_1 = 12
num_2 = 24
num_2 = 12

# Deklarasi variabel num_3 dengan hasil operasi aritmatika num_1 + num_2
num_3 = num_1 + num_2

print("num_3 =", num_3)  # Output: num_3 = 24


# Operator perbandingan
res = 4 == 5
print("4 == 5 =", res)  # Output: 4 == 5 = False

res = 4 != 5
print("4 != 5 =", res)  # Output: 4 != 5 = True

res = 4 > 5
print("4 > 5 =", res)  # Output: 4 > 5 = False

res = 4 < 5
print("4 < 5 =", res)  # Output: 4 < 5 = True

res = 5 >= 5
print("5 >= 5 =", res)  # Output: 5 >= 5 = True

res = 4 <= 5
print("4 <= 5 =", res)  # Output: 4 <= 5 = True

# Operator logika
res = (4 == 5) and (2 != 3)
print("(4 == 5) and (2 != 3) =", res)  # Output: (4 == 5) and (2 != 3) = False

res = (4 == 5) or (2 != 3)
print("(4 == 5) or (2 != 3) =", res)  # Output: (4 == 5) or (2 != 3) = True

res = not (2 == 3)
print("not (2 == 3) =", res)  # Output: not (2 == 3) = True


# Operator keanggotaan (in)
# Operasi keanggotaan pada list
sample_list = [2, 3, 4]
is_3_exists = 3 in sample_list
print("is 3 exists in sample_list:", is_3_exists)  # Output: is 3 exists in sample_list: True

# Operasi keanggotaan pada tuple
sample_tuple = ("hello", "python")
is_hello_exists = "hello" in sample_tuple
print("is 'hello' exists in sample_tuple:", is_hello_exists)  # Output: is 'hello' exists in sample_tuple: True

# Operasi keanggotaan pada dictionary (pengecekan kunci)
sample_dict = {"nama": "noval", "age": 12}
is_key_nama_exists = "nama" in sample_dict
print("is 'nama' exists in sample_dict:", is_key_nama_exists)  # Output: is 'nama' exists in sample_dict: True

# Operasi keanggotaan pada set
sample_set = {"sesuk", "preiiii"}
is_prei = "preiiii" in sample_set
print("is 'preiiii' exists in sample_set:", is_prei)  # Output: is 'preiiii' exists in sample_set: True

# Operasi keanggotaan pada string (pemeriksaan substring)
text = 'Hello world'
is_substring_exists = 'orl' in text
print("is 'orl' substring exists in 'Hello world':", is_substring_exists)  # Output: is 'orl' substring exists in 'Hello world': True


# Operator bitwise
# Operasi bitwise AND
x = 4 & 5  # 4 = 0100, 5 = 0101, hasil: 0100 = 4
print("4 & 5 =", x)  # Output: 4 & 5 = 4

# Operasi bitwise OR
x = 4 | 5  # 4 = 0100, 5 = 0101, hasil: 0101 = 5
print("4 | 5 =", x)  # Output: 4 | 5 = 5

# Operasi bitwise NOT
x = ~4  # 4 = 0100, hasil: 1011 = -5 (di dalam representasi complement dua)
print("~4 =", x)  # Output: ~4 = -5

# Operasi bitwise XOR
x = 4 ^ 5  # 4 = 0100, 5 = 0101, hasil: 0001 = 1
print("4 ^ 5 =", x)  # Output: 4 ^ 5 = 1

# Operasi bitwise right shift
x = 4 >> 2  # 4 = 0100, hasil: 0001 = 1
print("4 >> 2 =", x)  # Output: 4 >> 2 = 1

# Operasi bitwise left shift
x = 4 << 2  # 4 = 0100, hasil: 10000 = 16
print("4 << 2 =", x)  # Output: 4 << 2 = 16


# Operator identity (is)
# Memeriksa apakah dua objek memiliki identitas yang sama
# Bisa saja dua objek bernilai sama tapi memiliki identitas yang berbeda
num_1 = 100001
num_2 = 100001

res = num_1 is num_2
print("num_1 is num_2 =", res)  # Output: num_1 is num_2 = False
print("id(num_1):", id(num_1), "id(num_2):", id(num_2))

# Penulisan di atas sama saja dengan ini
# print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))
