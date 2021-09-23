"""21.Write a program in Python to initialize the items to the list and then display their sum to
the output console."""

n = int(input("How many numbers you want to enter in the list:"))

l = []

for i in range(0, n):
    x = int(input("Enter the item: "))
    l.append(x)

print("the sum of the item in the list is: ", sum(l))