# Menggandakan setiap angka dalam rentang 0-4
seq = [i * 2 for i in range(5)]
print(seq)  # output ➜ [0, 2, 4, 6, 8]

# Menyaring angka ganjil dalam rentang 0-9
seq = [i for i in range(10) if i % 2 == 1]
print(seq)  # output ➜ [1, 3, 5, 7, 9]

# Mengalikan angka dengan 2 jika genap, dan dengan 3 jika ganjil, dalam rentang 1-9
seq = [i * (2 if i % 2 == 0 else 3) for i in range(1, 10)]
print(seq)  # output ➜ [3, 4, 9, 8, 15, 12, 21, 16, 27]

# Menggabungkan setiap elemen dari dua list menjadi satu
list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']
seq = [x + y for x in list_x for y in list_y]
print(seq)  # output ➜ ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# Menghasilkan transposisi dari sebuah matriks
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)  # output ➜ [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Menghitung panjang setiap kata dalam daftar kata
words = ['apple', 'banana', 'cherry']
word_lengths = [len(word) for word in words]
print(word_lengths)  # output ➜ [5, 6, 6]

# Mengkuadratkan setiap angka dalam daftar angka
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # output ➜ [1, 4, 9, 16, 25]

# Mengubah list yang telah disematkan menjadi list datar
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)  # output ➜ [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Menghitung jumlah setiap huruf vokal dalam setiap kata dalam daftar string
string_list = ['hello', 'world', 'python']
vowel_count = [word.count(vowel) for word in string_list for vowel in 'aeiou']
print(vowel_count)  # output ➜ [2, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1]

# Menghitung jumlah diagonal dalam matriks
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
print(diagonal_sum)  # output ➜ 15

# Menemukan angka genap dalam rentang 0-9 dan mengkuadratkannya
even_squared = [num ** 2 for num in range(10) if num % 2 == 0]
print(even_squared)  # output ➜ [0, 4, 16, 36, 64]

# Menggabungkan dua list dan mengambil angka yang lebih besar dari 5
list_a = [3, 7, 1, 9]
list_b = [5, 2, 8, 6]
combined_greater_than_5 = [max(x, y) for x in list_a for y in list_b if max(x, y) > 5]
print(combined_greater_than_5)  # output ➜ [7, 9, 8, 6]

# Membuat daftar tuple dari dua list
list_x = ['a', 'b', 'c']
list_y = [1, 2, 3]
tuple_list = [(x, y) for x in list_x for y in list_y]
print(tuple_list)  # output ➜ [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

# enghasilkan daftar angka dari 0 hingga 9 dalam format string
number_strings = [str(num) for num in range(10)]
print(number_strings)  # output ➜ ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Menggabungkan dua list dan menghilangkan duplikat
list_a = [1, 2, 3]
list_b = [3, 4, 5]
combined_unique = list(set(list_a + list_b))
print(combined_unique)  # output ➜ [1, 2, 3, 4, 5]
