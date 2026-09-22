# 1.Write a PYTHON program to evaluate the student performance
#If % is >=90 then Excellent performance
#If % is >=80 then  Very Good performance
#If % is >=70 then Good performance
#If % is >=60 then average performance

nilai = int(input("Masukkan nilainya: "))

if nilai >= 90:
    print("Excellent")
elif nilai >= 80:
    print("Very Good")
elif nilai >= 70:
    print("Good")
elif nilai >= 60:
    print("Average")
else:
    print("Poor")