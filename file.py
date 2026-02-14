ile = open('codinal.txt')

print(file.read())

file.close()

file_read = open('codinal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('codinal.txt', 'w')

file_write.write("File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()

file_append = open('codinal.txt', 'a')

file_append.write("\n File in append mode ....")
file_append.write("Hi! I aPenguin. I am 1 yr. old")
file_append.close()
file = open("codinal.txt","r")
Counter = 0

Content = file.read()


CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is th number of lines in the file")
print(Counter)
firstfile = input("Enter the name of first file ")
secondfile = input("Enter the name of second file ")

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print('content of first file before appending -\n', f1.read())
print('content of second file before appending -\n', f2.read())

f1.close()
f2.close()

f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print('cotent of first file after append - \n', f1.read())
print('content od second file after appending - \n', f2.read())

f1.close()
f2.close()
