import mysql.connector
import os
from menu import Menu
from datetime import date


db = mysql.connector.connect(
			host="localhost",
  			user="root",
 			passwd="",
            database= "mrjuice")


def del_cust(np):
    curs = db.cursor()
    del_cust = """
				DELETE from pembeli where nama_pembeli = '{}'
				""".format(np)
    curs.execute(del_cust)
    db.commit()


def del_order(kode_jus):
    curs = db.cursor()
    del_order = "DELETE from order_jus where kode_jus = {}".format(kode_jus)
    curs.execute(del_order)
    db.commit()

# menu = Menu()
tgl = date.today()

class Admin:
    def __init__(self,username,password):
        self.username = username
        self.user_pw = password
    def desc_user(self):
        print("login succesfull")
        print(f"welcome again {self.username}")
    def verifikasi(self):
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
                os.system("cls")
                if  self.username  == uname and self.user_pw == upw:
                    self.desc_user()
                else:
                    print("Login failed")

#jus
class Jus(Menu):
    def __init__(self):
        super().__init__()

    def menu_adm_jus(self):
        Menu.h_juice(self)
        pilih = input("pilihan anda : ")
        if pilih == "1":
            self.list_jus()
            print("0.kembali")
            pilih2 = input("pilihan :")
            os.system("cls")
            self.menu_adm_jus()
        elif pilih == "2":
            self.del_jus()
            print("0.kembali")
            pilih2 = input("pilihan :")
            os.system("cls")
            self.menu_adm_jus()
        elif pilih == "3":
            self.update_jus()
            print("0.kembali")
            pilih2 = input("pilihan :")
            os.system("cls")
            self.menu_adm_jus()
        elif pilih == "4":
            self.insert_jus()
            print("0.kembali")
            pilih2 = input("pilihan :")
            os.system("cls")
            self.menu_adm_jus()
    def list_jus(self):
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


    def insert_jus(self):
        self.list_jus()
        cursor = db.cursor()
        nama_jus = input("jus : ")
        harga_jus = input("Harga : ")
        val = (nama_jus,harga_jus)
        sql = "insert into jus (nama_jus,harga_jus) values (%s,%s)"
        cursor.execute(sql, val)
        db.commit()
        os.system("clear")
        print("{} data berhasil disimpan".format(cursor.rowcount))
        self.list_jus()

    def update_jus(self):
        self.list_jus()
        cursor = db.cursor()
        kode_jus = input("Jus yang ingin di update : ")
        nama_jus = input("Ganti nama jus : ")
        harga_jus = input("Harga jus : ")
        val = (nama_jus,harga_jus,kode_jus)
        sql = "update jus set nama_jus =%s,harga_jus = %s WHERE kode_jus=%s"
        cursor.execute(sql, val)
        db.commit()
        os.system("clear")
        print("{} data berhasil diubah".format(cursor.rowcount))
        self.list_jus()
    def del_jus(self):
        self.list_jus()
        cursor = db.cursor()
        kode_jus = input("Jus yang ingin dihapus : ")
        sql = "DELETE FROM jus WHERE kode_jus={}".format(kode_jus)
        cursor.execute(sql)
        db.commit()
        os.system("clear")
        print("{} data berhasil dihapus".format(cursor.rowcount))
        self.list_jus()









        
#customer
class Customer():
    def __init__(self):
        pass

    def list_cust(self):
        print("-" * 116)
        print(
            "|  ID \t| k_jus |  jus \t |    order \t|  total_order \t |  metod_pembayaran\t|  pembeli |\t tanggal_pembelian |")

        print("-" * 116)
        cursor = db.cursor()
        cursor2 = db.cursor(buffered=True)
        cursor4 = db.cursor(buffered=True)

        sql = """
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

            sel_nama_pembeli = "SELECT nama_pembeli FROM pembeli"
            cursor2.execute(sel_nama_pembeli)
            results2 = cursor2.fetchone()
            nama = results2[0]

            sel_nama_pembeli2 = "SELECT nama_pembeli FROM pembeli "
            cursor4.execute(sel_nama_pembeli2)
            results4 = cursor4.fetchone()
            nama2 = results4[-1]

            for data in results:
                print("| ", data[0], "\t   ", data[1], " \t  ", data[2], "\t ", data[3], " \t      ", data[4], "\t\t ",
                      data[5], "\t\t  ", nama2, "\t  ", tgl, "  |")
            print("-" * 116)
            del_cust(nama)
            kode_jus = data[1]
            del_order(kode_jus)



