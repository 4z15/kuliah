import mysql.connector
import os
import pyfiglet
from datetime import date



db = mysql.connector.connect(
			host="localhost",
  			user="root",
 			passwd="",
  			database= "mrjuice")

def admin_menu():
	print("-"*15,"ADMIN MENU","-"*15)
	print(" ")
	print("\t\t1. List Customer")
	print("\t\t2. JUICE")
	print("\t\t0. Log Out")
	print(" ")
	print("-"*42)

def h_juice():
	print("-"*15,"JUICE MENU","-"*15)
	print(" ")
	print("\t\t1. List JUICE")
	print("\t\t2. DELETE JUICE")
	print("\t\t3. UPDATE JUICE")
	print("\t\t4. INSERT JUICE")
	print("\t\t0. BACK")
	print(" ")
	print("-"*42)

def h_customer():
	print("-"*15,"CUSTOMER MENU","-"*15)
	print(" ")
	print("\t\t1. List CUSTOMER")
	print("\t\t0. BACK")
	print(" ")
	print("-"*42)



def insert_pembeli(id_order,total_pembayaran,metod_pembayaran):
	val = (id_order,total_pembayaran,metod_pembayaran)
	curs2 = db.cursor()
	sql2 = "INSERT INTO `pembayaran` (`id_pembayaran`, `id_order`, `total_pembelian`, `metod_pembayaran`) VALUES (NULL, '{}', '{}', '{}')".format(id_order,total_pembayaran,metod_pembayaran)
	curs2.execute(sql2)
	db.commit()

def del_cust(np):
	curs = db.cursor()
	del_cust = 	"""
				DELETE from pembeli where nama_pembeli = '{}'
				""".format(np)
	curs.execute(del_cust)
	db.commit()
	

def del_order(kode_jus):
	curs = db.cursor()
	del_order = "DELETE from order_jus where kode_jus = {}".format(kode_jus)
	curs.execute(del_order)
	db.commit()




def h_metod_pembayaran():
	M_pembayaran = ["BCA","DANA","PAYPAL"]
	print("-"*27)
	print("| ID\t Metod_Pembayaran |")
	print("-"*27)
	for metode in range(len(M_pembayaran)):
		print("|",metode,"\t",M_pembayaran[metode],"\t\t  |")
	print("-"*27)

def h_transaksi():
		print("-"*50)
		print("\t\t  TRANSAKSI")
		print("-"*50)
		print("| ID   | K_JUS |  N_JUS   | HARGA   | J_ORDER    |")
		print("-"*50)

def h_pembayaran():
		print("-"*50)
		print("\t\t  PEMBAYARAN")
		print("-"*50)
		print("1.NON TUNAI")
		print("2.TUNAI")
		print("-"*50)

def h_menu():
	c = """ d[-_-]b"""
	result = pyfiglet.figlet_format("MR JUICE", font = "cosmic" )
	print("="*73)
	print(" ")
	print(result)
	print("\t\t\t\t\t\tBy : Rifky Azis",c)
	print("="*73)
	print("\t\t\t\t 1. Admin ")
	print("\t\t\t\t 2. Customer ")
	print("\t\t\t\t 0. Keluar")

tgl = date.today()
class MrJuice():
	"""docstring for ClassName"""
	def __init__(self):
		# self.
		self.nama = None
	

	def user(self):
		nama = input("nama anda : ")
		curs = db.cursor()
		sql = "INSERT INTO pembeli (nama_pembeli,tanggal_beli) VALUES ('{}','{}')".format(nama,tgl)
		curs.execute(sql)

		db.commit()
		print("selamat datang ",nama)


	def login_user(self):
		print("-"*15,"ADMIN MENU","-"*15)
		print(" ")
		cursor = db.cursor()
		sql = "select * from user "
		cursor.execute(sql)
		results = cursor.fetchall()
		if cursor.rowcount < 0:
			print("Tidak ada data")
		else:
			for data in results:
				uname = data[1]
				upw = data[2]
				user = input("username : ")
				pwd =  input("password : ")
				os.system("cls")
				if user == uname and pwd == upw:
					print("Login succesful")
					print("Welcome again  ",user)
				else:
					print("Login failed")


	def showcustomer(self):
		print("-"*116)
		print("|  ID \t| k_jus |  jus \t |    order \t|  total_order \t |  metod_pembayaran\t|  pembeli |\t tanggal_pembelian |")

		print("-"*116)
		cursor = db.cursor()
		cursor2 = db.cursor(buffered = True)
		cursor4 = db.cursor(buffered = True)



		sql = 	"""
				SELECT oj.id_order,j.kode_jus, j.nama_jus ,oj.jumlah_order,p.total_pembelian,p.metod_pembayaran
				FROM ((order_jus oj INNER JOIN jus j 
				ON oj.kode_jus = j.kode_jus)
				INNER JOIN pembayaran p 
				on p.id_order = oj.id_order)
				"""
		cursor.execute(sql)
		results = cursor.fetchall()
		

		if cursor.rowcount < 0:
			print("Tidak ada data")

		else:
		
			sel_nama_pembeli =  "SELECT nama_pembeli FROM pembeli"
			cursor2.execute(sel_nama_pembeli)
			results2 = cursor2.fetchone()
			nama = results2[0]
	

			sel_nama_pembeli2 =  "SELECT nama_pembeli FROM pembeli "
			cursor4.execute(sel_nama_pembeli2)
			results4 = cursor4.fetchone()
			nama2 = results4[-1]


			for data in results:
				print("| ",data[0], "\t   ",data[1], " \t  ",data[2], "\t " , data[3], " \t      " , data[4],"\t\t ", data[5],"\t\t  ",nama2,"\t  ",tgl,"  |")
			print("-"*116)
			del_cust(nama)
			kode_jus = data[1]
			del_order(kode_jus)
			



	def customer(self):
		h_customer()
		pilih = input("Pilihan anda : ")
		os.system("cls")
		if pilih  == "1":
			self.showcustomer()
			print("0.kembali")
			pilih2 = input("pilihan :")
			os.system("cls")
			self.customer()
			
		elif pilih == "0":
			menu()

	def update_juice(self):
		self.show_datajus()
		cursor = db.cursor()
		kode_jus = input("Jus yang ingin di update : ")
		nama_jus = input("Ganti nama jus : ")
		harga_jus = input("Harga jus : ")
		val = (nama_jus,harga_jus,kode_jus)
		sql = "update jus set nama_jus =%s,harga_jus = %s WHERE kode_jus=%s"
		cursor.execute(sql, val)
		db.commit()
		os.system("cls")
		print("{} data berhasil diubah".format(cursor.rowcount))
		self.show_datajus()




	def del_juice(self):
		self.show_datajus()
		cursor = db.cursor()
		kode_jus = input("Jus yang ingin dihapus : ")
		sql = "DELETE FROM jus WHERE kode_jus={}".format(kode_jus)
		cursor.execute(sql)
		db.commit()
		os.system("cls")
		print("{} data berhasil dihapus".format(cursor.rowcount))
		self.show_datajus()


	def insert_juice(self):
  		self.show_datajus()
  		cursor = db.cursor()
  		nama_jus = input("jus : ")
  		harga_jus = input("Harga : ")
  		val = (nama_jus,harga_jus)
  		sql = "insert into jus (nama_jus,harga_jus) values (%s,%s)"
  		cursor.execute(sql, val)
  		db.commit()
  		os.system("cls")
  		print("{} data berhasil disimpan".format(cursor.rowcount))
  		self.show_datajus()



 		
	def juice(self):
		h_juice()
		pilih = input("Pilihan anda : ")
		os.system("cls")
		if pilih  == "1":
			self.show_datajus()
			print("0.kembali")
			pilih2 = input("pilihan :")
			os.system("cls")
			self.juice()
			
		elif pilih == "2":
			self.del_juice()
			print("0.kembali")
			pilih2 = input("pilihan :")
			os.system("cls")
			self.juice()
		elif pilih == "3":
			self.update_juice()
			print("0.kembali")
			pilih2 = input("pilihan :")
			os.system("cls")
			self.juice()
		elif pilih == "4":
			self.insert_juice()
			print("0.kembali")
			pilih2 = input("pilihan :")
			os.system("cls")
			self.juice()
		elif pilih == "0":
			menu()
		else:
			print("Menu tidak ada ")

	def show_datajus(self):
		print("-"*55)
		print("\t\t\t MENU")
		print("-"*55)
		print("| ID | \t\t |    JUS    | \t\t | HARGA |")
		print("-"*55)
		cursor = db.cursor()
		sql = "select * from jus"
		cursor.execute(sql)
		results = cursor.fetchall()
		if cursor.rowcount < 0:
			print("Tidak ada data")
		else:
			for data in results:
				print("| ",data[0]," |","\t","| ",data[1]," |", "\t\t",   " | ", data[2], " |")
				if data == 0:
					break

			print("-"*55)



	def transaksi(self):
		curs2 = db.cursor()
		pilih = int(input("Mau pilih jus yang mana : "))
		order = int(input("Mau beli  berapa: "))
		val = (pilih,order)
		sql2 = "INSERT INTO `order_jus` (`id_order`, `kode_jus`, `jumlah_order`) VALUES (NULL, '%s', '%s')"
		curs2.execute(sql2, val)
		db.commit()
		os.system("cls")

		sql = "SELECT order_jus.id_order,  jus.kode_jus,jus.nama_jus ,jus.harga_jus,order_jus.jumlah_order  FROM order_jus INNER JOIN jus ON order_jus.kode_jus = jus.kode_jus  where order_jus.kode_jus = {}".format(pilih)
		h_transaksi()

		
		curs2.execute(sql)
		results = curs2.fetchall()
		if curs2.rowcount < 0:
			print("Tidak ada data")
		else:
			for data in results:
				# print(data)
				print("| ",data[0]," | ",data[1],"   |" , data[2],"    |",data[3], "  | ",data[4], "        | ")
			print("-"*50)

			id_order = data[0]
			harga = data[3]
			jumlah_order = data[4]
			total_order = harga * jumlah_order 
	
			# os.system("cls")
			print("Total pembelian : ", total_order)  
			
			h_pembayaran()
			M_pembayaran = ["BCA","DANA","PAYPAL","CASH"]

			pilih_pembayaran = input("Masukkan metode pembayaran anda : ")
			os.system("cls")

			if pilih_pembayaran == '1':
				h_metod_pembayaran()
				metod_pembayaran = input("metode pembayaran pilihan anda :  ")
				os.system("cls")

				if metod_pembayaran == '0':
					no_rek = input("No Rekening anda : ")
					pwd_BCA = input("Password : ")
					print("melakukan pembayaran.........")
					print("pembayaran berhasil")
					print("Terima kasih telah belanja di MRJUICE")
					insert_pembeli(id_order,total_order,M_pembayaran[0])
					menu()

				elif metod_pembayaran == '1':
					no_Hp= input("No HP anda : ")
					pin_dana = input("Password : ")
					print("melakukan pembayaran.........")
					print("pembayaran berhasil")
					print("Terima kasih telah belanja di MRJUICE")
					insert_pembeli(id_order,total_order,M_pembayaran[1])
					os.system("cls")

					menu()


				elif metod_pembayaran == '2':
					email= input("email paypal anda  : ")
					pwd = input("Password : ")
					print("melakukan pembayaran.........")
					print("pembayaran berhasil")
					print("Terima kasih telah belanja di MRJUICE")
					insert_pembeli(id_order,total_order,M_pembayaran[2])
					os.system("cls")
					menu()


				else:
					print("Maaf metode pembayaran ",metod_pembayaran,"tidak ada di MRJUICE")
					
			elif pilih_pembayaran == '2':
				uang_pembayaran = float(input("Uang untuk membayar : "))

				if uang_pembayaran == total_order:
					os.system("cls")
					print("Terima kasih telah belanja di MRJUICE")
					insert_pembeli(id_order,total_order,M_pembayaran[3])
					menu()


				elif uang_pembayaran > total_order:
					os.system("cls")
					kembalian = uang_pembayaran - total_order
					print("Kembalian anda : ",kembalian)
					print("Terima kasih telah belanja di MRJUICE")
					insert_pembeli(id_order,total_order,M_pembayaran[3])
					menu()


			else:
				print("Maaf metode pembayaran ",pilih_pembayaran,"tidak ada di MRJUICE")



		








def menu():
	test = MrJuice()
	h_menu()
	pilih = input("pilihan anda : ")

	os.system("cls")

	if pilih == "1":
		test.login_user()
		admin_menu()
		pilih2 = input("pilihan anda : ")
		os.system("cls")
		if pilih2 == "1":
			test.customer()
		elif pilih2 == "2":
			test.juice()
		elif pilih2 == "0":
			print("THANK YOU FOR COMING  , HAVE A NICE DAY ")
			exit()
		else:
			print(pilih2,"Menu tidak ada ")
		
	elif pilih == '2':
		test.user()
		test.show_datajus()
		test.transaksi()
	elif pilih == "0":
		print("THANK YOU FOR COMING  , HAVE A NICE DAY ")
		exit()
	else:
		print("Menu tidak ada ")


menu()




