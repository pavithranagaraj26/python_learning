# file =open("demo.txt",'w')
# #do something with the file
# file.close()

file =open("demo.txt",'r')
#do something with the file
content=file.readline()
print(content)
file.close()