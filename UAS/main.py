from menu import *
from admin import Admin,Jus,Customer
from Customer import customer
import os

menu = Menu()
adm_cust = Customer()
adm_jus = Jus()
cust = customer()



def main():
    menu.h_menu()
    pilih = input("pilihan anda : ")
    os.system("cls")

    if pilih == "1":
        user = input("username : ")
        pw = input("password : ")
        admin = Admin(user,pw)
        admin.verifikasi()
        menu.admin_menu()
        pilih2 = input("pilihan anda : ")
        os.system("cls")
        if pilih2 == "1":
            adm_cust.list_cust()
        elif pilih2 == "2":
            adm_jus.menu_adm_jus()
        elif pilih2 == "0":
            print("THANK YOU FOR COMING  , HAVE A NICE DAY ")
            exit()
        else:
            print(pilih2, "Menu tidak ada ")

    elif pilih == '2':
        cust.cust()
        cust.show_datajus()
        cust.transaksi()
    elif pilih == "0":
        print("THANK YOU FOR COMING  , HAVE A NICE DAY ")
        exit()
    else:
        print("Menu tidak ada ")
main()


