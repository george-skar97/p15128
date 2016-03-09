from PIL import Image 
im = Image.open("test.jpg")
rgb_im = im.convert('RGB')
n= raw_input("Δώσε την πάνω αριστερά γωνία του πίνακα")
n=int(n)
for i in range(n,(n+3)):
	for j in range(n,(n+3)):
		r, g, b = rgb_im.getpixel((j, i))
#print r,g,b
		pix=r+g+b 
		if ((pix <= 95) and (pix >= 0) ):
			print (" "),
		elif ((pix > 95)and(pix<=191) ):
			print("."),
		elif ((pix > 191)and(pix<=286) ):
			print(","),
		elif ((pix > 286)and(pix<=381) ):
			print("-"),
		elif ((pix > 381)and(pix<=476) ):
			print("*"),
		elif ((pix > 476)and(pix<=571) ):
			print("#"),
		elif ((pix > 571)and(pix<=667) ):
			print("&"),
		else:
			print("@"),
	print("\n"),
			
