kolom = 6
for i in range(0,kolom):
	for j in range(0,kolom-1):
		print("*", end =" ")
	kolom -=1
	print(" ")

baris = 5
for i in range(0,baris):
	for j in range(0,i+1):
		print("*", end=" ")
	print(" ")
	

