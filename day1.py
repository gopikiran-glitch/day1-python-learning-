Understanding Hello World Program in Python
The following is a simple program that displays the message “Hello, World!” on the screen.




# This is a comment. It will not be executed.
print("Hello, World!")

Output
Hello, World!
Python Applications and Advantages
Last Updated : 03 Oct, 2025
Python is a high-level, interpreted, and general-purpose dynamic programming language that focuses on code readability. It generally has small programs when compared to Java and C.


Take Multiple Input in Python
We are taking multiple input from the user in a single line, splitting the values entered by the user into separate variables for each value using the split() method. Then, it prints the values with corresponding labels, either two or three, based on the number of inputs provided by the user.


# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
Output

Enter two values: 5 10
Number of boys:  5  
Number of girls:  10
Enter three values: 5 10 15
Total number of students:  5
Number of boys is :  10     
Number of girls is :  15  




Python Variables
Last Updated : 15 Oct, 2025
In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.

Unlike Java and many other languages, Python variables do not require explicit declaration of type.
The type of the variable is inferred based on the value assigned.



# Variable 'x' stores the integer value 5
x = 5
​
# Variable 'name' stores the string "Samantha"
name = "Samantha"  
​
print(x)
print(name)

Output
5
Samantha



# operators_demo.py
# Demonstrates many Python operators with small, runnable examples.

# Arithmetic operators
a = 10
b = 3
print("Arithmetic:")
print("a + b =", a + b)       # addition
print("a - b =", a - b)       # subtraction
print("a * b =", a * b)       # multiplication
print("a / b =", a / b)       # true division
print("a // b =", a // b)     # floor division
print("a % b =", a % b)       # modulus
print("a ** b =", a ** b)     # exponentiation
print()

# Unary + and -
x = -5
print("Unary:")
print("+x =", +x)
print("-x =", -x)
print()

# Assignment and augmented assignment
c = 5
print("Assignment and augmented assignment:")
print("initial c =", c)
c += 2   # c = c + 2
print("c += 2 ->", c)
c *= 3   # c = c * 3
print("c *= 3 ->", c)
c //= 4  # c = c // 4
print("c //= 4 ->", c)
c **= 2  # c = c ** 2
print("c **= 2 ->", c)
c &= 7   # bitwise AND assignment
print("c &= 7 ->", c)
c |= 2   # bitwise OR assignment
print("c |= 2 ->", c)
c ^= 1   # bitwise XOR assignment
print("c ^= 1 ->", c)
c <<= 1  # left shift assignment
print("c <<= 1 ->", c)
c >>= 2  # right shift assignment
print("c >>= 2 ->", c)
print()

# Comparison operators and chained comparisons
p = 4
q = 7
print("Comparison:")
print("p == q ->", p == q)
print("p != q ->", p != q)
print("p < q ->", p < q)
print("p <= q ->", p <= q)
print("p > q ->", p > q)
print("p >= q ->", p >= q)
print("1 < p < 10 ->", 1 < p < 10)  # chained comparison
print()

# Logical operators
print("Logical:")
t = True
f = False
print("t and f ->", t and f)
print("t or f ->", t or f)
print("not t ->", not t)
# Bitwise operators
print("Bitwise:")
u = 0b1010  # 10
v = 0b0110  # 6
print("u =", bin(u), "v =", bin(v))
print("u & v =", bin(u & v))
print("u | v =", bin(u | v))
print("u ^ v =", bin(u ^ v))
print("~u =", bin(~u))   # bitwise NOT (two's complement)
print("u << 2 =", bin(u << 2))
print("v >> 1 =", bin(v >> 1))
print()

# Membership operators
print("Membership:")
lst = [1, 2, 3, 4]
print("2 in lst ->", 2 in lst)
print("5 not in lst ->", 5 not in lst)
s = "hello"
print("'ell' in s ->", 'ell' in s)
print()

# Identity operators
print("Identity:")
a1 = [1, 2, 3]
a2 = a1
a3 = list(a1)  # creates a new list with same contents
print("a1 is a2 ->", a1 is a2)      # True: same object
print("a1 is a3 ->", a1 is a3)      # False: different objects
print("a1 == a3 ->", a1 == a3)      # True: equal contents
print()

# Ternary conditional operator
print("Ternary:")
n = 5
parity = "even" if n % 2 == 0 else "odd"
print("n is", n, "->", parity)
print()

import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)
