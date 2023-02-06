import mysql.connector
import os
from menu import Menu
from datetime import date


db = mysql.connector.connect(
			host="localhost", 
  			user="root",
 			passwd="",
            database= "mrjuice")
tgl = date.today()
def insert_pembeli(id_order,total_pembayaran,metod_pembayaran):
	val = (id_order,total_pembayaran,metod_pembayaran)
	curs2 = db.cursor()
	sql2 = "INSERT INTO `pembayaran` (`id_pembayaran`, `id_order`, `total_pembelian`, `metod_pembayaran`) VALUES (NULL, '{}', '{}', '{}')".format(id_order,total_pembayaran,metod_pembayaran)
	curs2.execute(sql2)
	db.commit()

# menu = Menu()
class customer(Menu):
    def __init__(self):
        super().__init__()

    def cust(self):
        nama = input("nama anda : ")
        curs = db.cursor()
        sql = "INSERT INTO pembeli (nama_pembeli,tanggal_beli) VALUES ('{}','{}')".format(nama, tgl)
        curs.execute(sql)

        db.commit()
        print("selamat datang ", nama)

    def show_datajus(self):
        print("-" * 55)
        print("\t\t\t MENU")
        print("-" * 55)
        print("| ID | \t\t |    JUS    | \t\t | HARGA |")
        print("-" * 55)
        cursor = db.cursor()
        sql = "select * from jus"
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                print("| ", data[0], " |", "\t", "| ", data[1], " |", "\t\t", " | ", data[2], " |")
                if data == 0:
                    break

            print("-" * 55)

    def transaksi(self):
        curs2 = db.cursor()
        pilih = int(input("Mau pilih jus yang mana : "))
        order = input("Mau beli  berapa: ")
        val = (pilih, int(order))
        sql2 = "INSERT INTO `order_jus` (`id_order`, `kode_jus`, `jumlah_order`) VALUES (NULL, '%s', '%s')"
        curs2.execute(sql2, val)
        db.commit()
        os.system("cls")

        sql = "SELECT order_jus.id_order,  jus.kode_jus,jus.nama_jus ,jus.harga_jus,order_jus.jumlah_order  FROM order_jus INNER JOIN jus ON order_jus.kode_jus = jus.kode_jus  where order_jus.kode_jus = {}".format(
            pilih)
        # menu.h_transaksi()
        Menu.h_transaksi(self)

        curs2.execute(sql)
        results = curs2.fetchall()
        if curs2.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                # print(data)
                print("| ", data[0], " | ", data[1], "   |", data[2], "    |", data[3], "  | ", data[4], "        | ")
            print("-" * 50)

            id_order = data[0]
            harga = data[3]
            jumlah_order = data[4]
            total_order = harga * jumlah_order

            # os.system("cls")
            print("Total pembelian : ", total_order)

            Menu.h_pembayaran(self)
            M_pembayaran = ["BCA", "DANA", "PAYPAL", "CASH"]

            pilih_pembayaran = input("Masukkan metode pembayaran anda : ")
            os.system("cls")

            if pilih_pembayaran == '1':
                Menu.h_metod_pembayaran(self)
                metod_pembayaran = input("metode pembayaran pilihan anda :  ")
                os.system("cls")

                if metod_pembayaran == '0':
                    no_rek = input("No Rekening anda : ")
                    pwd_BCA = input("Password : ")
                    print("melakukan pembayaran.........")
                    print("pembayaran berhasil")
                    print("Terima kasih telah belanja di MRJUICE")
                    insert_pembeli(id_order, total_order, M_pembayaran[0])


                elif metod_pembayaran == '1':
                    no_Hp = input("No HP anda : ")
                    pin_dana = input("Password : ")
                    print("melakukan pembayaran.........")
                    print("pembayaran berhasil")
                    print("Terima kasih telah belanja di MRJUICE")
                    insert_pembeli(id_order, total_order, M_pembayaran[1])
                    os.system("cls")




                elif metod_pembayaran == '2':
                    email = input("email paypal anda  : ")
                    pwd = input("Password : ")
                    print("melakukan pembayaran.........")
                    print("pembayaran berhasil")
                    print("Terima kasih telah belanja di MRJUICE")
                    insert_pembeli(id_order, total_order, M_pembayaran[2])
                    os.system("cls")



                else:
                    print("Maaf metode pembayaran ", metod_pembayaran, "tidak ada di MRJUICE")

            elif pilih_pembayaran == '2':
                uang_pembayaran = float(input("Uang untuk membayar : "))

                if uang_pembayaran == total_order:
                    os.system("cls")
                    print("Terima kasih telah belanja di MRJUICE")
                    insert_pembeli(id_order, total_order, M_pembayaran[3])



                elif uang_pembayaran > total_order:
                    os.system("cls")
                    kembalian = uang_pembayaran - total_order
                    print("Kembalian anda : ", kembalian)
                    print("Terima kasih telah belanja di MRJUICE")
                    insert_pembeli(id_order, total_order, M_pembayaran[3])



            else:
                print("Maaf metode pembayaran ", pilih_pembayaran, "tidak ada di MRJUICE")

