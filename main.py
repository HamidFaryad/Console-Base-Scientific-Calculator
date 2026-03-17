from cmath import atan

"""
Scientific Calculator
Make a menu-based calculator with many math operations.
Use import math for advanced functions.
Create separate functions for each operation in a file called operations.py.
Main file main.py shows menu and calls functions.

Features:

Addition, Subtraction, Multiplication, Division
Square, Cube, Custom Power (like x^y)
Square Root, Cube Root
Sin, Cos, Tan (and inverse: asin, acos, atan)
Log (base 10), Natural Log (ln), Antilog
Handle errors (like divide by zero)
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Square
6. Cube
7. Power (x^y)
8. Square Root
9. Cube Root
10. Sin
11. Cos
12. Tan
13. asin
14. acos
15. atan
16. Log (base 10)
17. Natural Log (ln)
18. Antilog
0. Exit
"""


import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    return a / b
def square (a):
    return a ** 2
def cube (a):
    return a ** 3
def squareRoot(a):
    return math.sqrt(a)
def cubeRoot(a):
    return math.cbrt(a)
def sin(a):
   return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def log(a):
    return math.log(a)
def asin(a):
    return math.asin(a)
def acos(a):
    return math.acos(a)


print("="*40)
print("""1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Square
6. Cube
7. Square Root
8. Cube Root
9. Sin,
10. Cos,
11. Tan,
12. asin,
13. acos,
14. atan
15. log (base 10)
16. Exit""")
print("="*40)
while True:
    choice= int(input("Enter your choice:"))
    if choice == 1:
        print("1. Addition")
        f_num = int(input("Enter first number:"))
        s_num = int(input("Enter second number:"))
        result = add(f_num, s_num)
        print("result:", result)
    elif choice == 2:
        print("2. Subtraction")
        f_num = int(input("Enter first number:"))
        s_num = int(input("Enter second number:"))
        result = sub(f_num, s_num)
        print("result:", result)
    elif choice == 3:
        print("3. Multiplication")
        f_num = int(input("Enter first number:"))
        s_num = int(input("Enter second number:"))
        result = multi(f_num, s_num)
        print("result:", result)
    elif choice == 4:
        print("4. Division")
        f_num = int(input("Enter first number:"))
        s_num = int(input("Enter second number:"))
        result = div(f_num, s_num)
        print("result:", result)
    elif choice == 5:
        print("5. Square")
        f_num = int(input("Enter first number:"))
        result =square(f_num)
        print("result:", result)
    elif choice == 6:
        print("Cube")
        f_num = int(input("Enter first number:"))
        result = cube(f_num)
        print("result:", result)
    elif choice ==7:
        print("Square Root")
        f_num = int(input("Enter first number:"))
        result = squareRoot(f_num)
        print("result:", result)
    elif choice == 8:
        print("Cube Root")
        f_num = int(input("Enter first number:"))
        result = cubeRoot(f_num)
        print("result:", result)
    elif choice == 9:
        print("Sin")
        f_num = int(input("Enter first number:"))
        result = sin(f_num)
        print("result:", result)
    elif choice == 10:
        print("Cos")
        f_num = int(input("Enter first number:"))
        result = cos(f_num)
        print("result:", result)
    elif choice == 11:
        print("Tan")
        f_num = int(input("Enter first number:"))
        result = tan(f_num)
        print("result:", result)
    elif choice == 12:
        print("asin")
        f_num = int(input("Enter first number:"))
        result = asin(f_num)
        print("result:", result)
    elif choice == 13:
        print("acos")
        f_num = int(input("Enter first number:"))
        result = acos(f_num)
        print("result:", result)
    elif choice == 14:
        print("atan")
        f_num = int(input("Enter first number:"))
        result = atan(f_num)
        print("result:", result)
    elif choice == 15:
        print("log")
        f_num = int(input("Enter first number:"))
        result = log(f_num)
        print("result:", result)
    elif choice == 16:
        print("Program Closed")
        break
    else:
        print("Invalid input")

