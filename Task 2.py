with open("output.txt",'w') as file:
    line=input("Enter text to write to the file: ")
    file.write(line+'\n')
print("Data successfully written to output.txt\n")

with open("output.txt",'a') as file:
    line=input("Enter additional text to append: ")
    file.write(line+'\n')
print("Data successfully appended.\n")

line=print("Final content of output.txt: ")
with open("output.txt",'r') as file:
    reading=file.read()
    print(reading)




