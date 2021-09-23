#24.Write a Python Program to read an entire text file and display the same to the screen.
#fname = input("Enter the name of file to open: ")

file = open("check.txt", "r")
print(file.strip())
words = file.strip()

print("Number of words in the file are: ", len(words))

file.close()