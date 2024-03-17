# Contoh penggunaan for dan range
for i in range(5):
    print("index:", i)

# Contoh penerapan fungsi range() dengan parameter start, stop, dan step
for i in range(1, 10, 2):
    print("index:", i)

# Iterasi data list
messages = ["pagi", "siang", "sore"]
for m in messages:
    print(m)

# Iterasi data tuple
numbers = ("dua puluh empat", 24)
for n in numbers:
    print(n)

# Iterasi data string
for char in "halo python":
    print(char)

# Iterasi data dictionary
bio = {
    "nama": "toyota camry",
    "tahun": 1993,
}
for key in bio:
    print("kunci:", key, "nilai:", bio[key])

# Iterasi data set
numbers = {"dua puluh empat", 24}
for n in numbers:
    print(n)

# Perulangan bercabang (nested loop)
maks = int(input("jumlah bintang: "))
for i in range(maks):
    for j in range(0, maks - i):
        print("*", end=" ")
    print()
