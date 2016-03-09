import random

rantable = [" ", 0]
produc = [[0 for x in range(8)] for x in range(8)]
for i in range(8):
	for j in range(8):
		produc[i][j] = random.choice(rantable)
print produc
product_file = open("base.txt", "w")
for i in range(8):
	product_file.write ('%s' % produc[i])
product_file.close()
tetris = [[0 for x in xrange(8)] for x in xrange(8)]
file_in = open ("base.txt")
for line in file_in:
    line = line.replace("'" , "")
    line = line.replace("][" , ", ")
    line = line.replace("]" , "")
    line = line.replace("[" , "")
file_in.close()
tmp = line.split(", ")
y = 0

for i in range(8):
    for j in range(8):
        tetris[i][j]= tmp[y]
        y +=1
print ("Αρχική μορφή του πίνακα:")
for i in range (8):
    for j in range (8):
        print tetris[i][j], (" "),
    print("\n")
for i in range(16):
    print "_",
print ("\n")
print ("Πρώτη περιστροφή:")
rotate90 = zip(*tetris[::-1])
for i in range (8):
    for j in range (8):
            print rotate90[i][j], (" "),
    print("\n")
for i in range(16):
    print "_",
print ("\n")
print ("Δεύτερη περιστροφή:")
rotate180 = zip(*rotate90[::-1])
for i in range (8):
    for j in range (8):
            print rotate180[i][j], (" "),
    print("\n")
for i in range(16):
    print "_",
print ("\n")
print ("Τρίτη περιστροφή:")
rotate270 = zip(*rotate180[::-1])
for i in range (8):
    for j in range (8):
            print rotate270[i][j], (" "),
    print("\n")