container = open("sample.txt" , "r")
print(container.readable())
for item in container.readlines() :
    print(item)
container.close()
