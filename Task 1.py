file=open("sample.txt",'r')
reading_file=file.read()
print(reading_file)

try:
    file=open("sample2.txt",'r')
    reading_file=file.read()
    print(reading_file)
except: FileNotFoundError
print("Error: The file 'sample2.txt' was not found ")

