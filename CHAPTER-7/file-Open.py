f = open("demo.txt", "rt")
# data = f.read(5)
line1 = f.readline()
print(line1)
print(type(line1))

f.close()