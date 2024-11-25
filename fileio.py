
#f = open("example.txt", "w")
#f.write("Hello \nGoodbye")
#f.close()

#f = open("example.txt", "r")
#print(f.readlines())
#content = f.read()
#print(content.split("\n"))
#f.close()

with open("example.txt", "w") as f:
    f.write("New info")