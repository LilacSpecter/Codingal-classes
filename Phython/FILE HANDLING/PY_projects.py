# File Handling project
# module 12, 1#
#file = open("sample_doc.txt", "w")
#file.write("student details")
#file.write("student name: Rowanne Coorey ")
#file.close()

#file = open("sample_doc.txt", "a")
#file.write("\nstudents favourite subjects: Science, I.C.T, English, French, History.\n\n")
#file.close()

#file = open("sample_doc.txt", "r")
#print(file.read())
#file.close()

#//// 2#
file = open("about bee's_doc.txt", "w")
file.write("BEE'S\n")
file.write(" Bee's create honey from pollen. \n And they are verry hardworking.\n")
file.write(" There are different types of bee's around the world.\n")
file.write("fun fact:\n Bee's honey can last up to more than 1000 years.\n Bee's honey was found in Egypt and it is still edible. \n")
file.write(" Bee's are amazing creatures if they are not there our gardens won't be the same,\n there will be no beautiful flowers to see.\n ")
file.write("Thus Bee's are amazing creatures.\n")
file.close()

print("printing the whole file:\n")
file = open("about bee's_doc.txt", "r")
print(file.read())
file.close()

print("printing the first 10 characters:\n")
file = open("about bee's_doc.txt", "r")
print(file.read(10))
file.close()

print("\nprinting the first line of the file:\n")
file = open("about bee's_doc.txt", "r")
print(file.readline())
file.close()

print("printing the first 4 lines of the file:\n")
file = open("about bee's_doc.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print("looping through the file\n")
file = open("about bee's_doc.txt","r")

for x in file:
 print(x)

file.close()


