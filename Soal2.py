#Write a PYTHON program to find largest of three numbers!

no1 = float(input("Menambahkan angka pertama: "))
no2 = float(input("Menambahkan angka kedua: "))
no3 = float(input("Menambahkan angka ketiga: "))

if (no1 >= no2) and (no1 >= no3):
    terbesar = no1
elif (no2 >= no1) and (no2 >= no3):
    terbesar = no2
else:
    terbesar = no3

print("Nomor terbesar adalah: ", terbesar)
