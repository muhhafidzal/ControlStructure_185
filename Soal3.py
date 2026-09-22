#Write a PYTHON program to print Fibonacci series up to n!

n = int(input("Enter n: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b