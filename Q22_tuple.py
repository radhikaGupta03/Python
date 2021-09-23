"""22.Write a program in Python to insert the names of cities accepted from the user into a
tuple. Display the same to the output screen."""
t1 = tuple()

n = int(input("How many cities you want to enter? "))

for i in range(n):
    a = input("Enter city: ")
    t1 = t1 + (a,)

print("The entered cities are: ")
for i in t1:
    print(i, end = " ")