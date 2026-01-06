#Activity 1
#write to a file
with open("sample.txt","w") as f :
    f.write("Hello World\nThis is Phython file handling\nFile operations are imporant.")

    #read to a file
with open("sample.txt", "r") as f:
    content = f.read()
    print("Full contend:\n", content)

#Split content into words and store in a List
words = content.split()
print("\nSplit words:", words)

# Close file (not needed when using 'with', it auto-closes.)