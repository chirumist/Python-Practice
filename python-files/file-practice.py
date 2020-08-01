"""
File io example
"""
f = open("test.txt", "r+")
print(f.read())
file = f.write(" thank you \n")
print(f.read())
f.close()