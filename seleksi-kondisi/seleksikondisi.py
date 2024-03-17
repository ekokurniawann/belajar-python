nilai = int(input("Masukkan nilai Anda: "))

# Seleksi kondisi untuk nilai
if nilai == 100:
    print("Sempurna!")
elif nilai >= 85:
    print("Hebat!")
elif nilai >= 65:
    print("Lulus")

    # Kondisi bersarang untuk nilai lulus
    if nilai <= 70:
        print("Namun, perlu adanya peningkatan!")
    else:
        print("Dengan nilai yang cukup baik")
else:
    print("Belum mencapai nilai yang memuaskan")
