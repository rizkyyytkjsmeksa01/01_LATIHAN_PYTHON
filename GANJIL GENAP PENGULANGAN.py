# ALAT PENGHITUNG ANGKA GANJIL DAN GENAP

while True:
    print("\n=== PENGECEKAN GANJIL / GENAP ===")
    print("Ketik 'q' untuk keluar dari program.")

    i = input("Masukkan Angka : ")

    # Tombol keluar
    if i.lower() == "q":
        print("Program selesai. Terima kasih!")
        break

    # Memastikan input berupa angka
    try:
        i = int(i)

        # LOGIKA PENGHITUNGAN
        if i % 2 == 0:
            print("Angka", i, "Termasuk Bilangan Genap")
        else:
            print("Angka", i, "Termasuk Bilangan Ganjil")

    except ValueError:
        print("Input tidak valid! Masukkan angka atau 'q' untuk keluar.")
        