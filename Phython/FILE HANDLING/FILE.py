#Activity 1
#write to a file
#with open("sample.txt","w") as f :
#    f.write("Hello World\nThis is Phython file handling\nFile operations are imporant.")

    #read to a file
#with open("sample.txt", "r") as f:
#    content = f.read()
#    print("Full contend:\n", content)

#Split content into words and store in a List
#words = content.split()
#print("\nSplit words:", words)

# Close file (not needed when using 'with', it auto-closes.)

# activity 1

# open file and read it's contents
#file = open('Codingal.txt','r')
#print(file.read())
#file.close()

#open file and read it's beginning 8 characters
#file = open('Codingal.txt','r')
#print("\n Read in parts \n")
#print(file.read(8))
#file.close()

#apped your name and age in the file
##file = open('Codingal.txt','a')
#file.write("Hi! I am Penguin and i am 1 yr old.")
#file.close()

#activity 2
# read first line of file
#file = open('Codingal.txt','r')
#print("Reading multiple lines...")
#print(file.readline())
#print(file.readline())
#print(file.readline())
#file.close()

#looping through alll lines of the file 
#file = open('Codingal.txt','r')
#print("Looping through the lines...")
#for lines in file:
#    print(line)
#file.close()

### 20/01/2026 ###

file_read = open("sample_doc.txt", "r")
print("file in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open("sample_doc.txt", "w")
file_write.write("1. file in write mode - \n")
file_write.write("Hi I am Penguin. I am 9 years old")
file_write.close()

file_append = open("sample_doc.txt", "a")
file_append.write("\n File in append mode - \n")
file_append.write("Hi! I am Penguin. I am 10 years old")
file_append.close()

file_write = open("sample_doc.txt", "w")
file_write.write("Hi!\nI AM PENGUIN. AND MY AGE IS INFINITY......")
file_write.close

#file_read = open("sample_doc.txt", "r")
#print("2. file in Read Mode -")
#print(file_read.read())
#file_print.close






