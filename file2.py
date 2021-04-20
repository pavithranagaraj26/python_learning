file=open("demo2.txt",'w')
file.write("three")
file.close()

file=open("demo2.txt",'r')
content=file.read()
print(content)