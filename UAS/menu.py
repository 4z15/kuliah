import pyfiglet

class Menu:
    def __init__(self):
        #print("menu-menu")
        pass
    def admin_menu(self):
        print("-"*15,"ADMIN MENU","-"*15)
        print(" ")
        print("\t\t1. List Customer")
        print("\t\t2. JUICE")
        print("\t\t0. Log Out")
        print(" ")
        print("-"*42)

    def h_juice(self):
        print("-"*15,"JUICE MENU","-"*15)
        print(" ")
        print("\t\t1. List JUICE")
        print("\t\t2. DELETE JUICE")
        print("\t\t3. UPDATE JUICE")
        print("\t\t4. INSERT JUICE")
        print("\t\t0. BACK")
        print(" ")
        print("-"*42)

    def h_customer(self):
        print("-"*15,"CUSTOMER MENU","-"*15)
        print(" ")
        print("\t\t1. List CUSTOMER")
        print("\t\t0. BACK")
        print(" ")
        print("-"*42)

    def h_metod_pembayaran(self):
        M_pembayaran = ["BCA", "DANA", "PAYPAL"]
        print("-" * 27)
        print("| ID\t Metod_Pembayaran |")
        print("-" * 27)
        for metode in range(len(M_pembayaran)):
            print("|", metode, "\t", M_pembayaran[metode], "\t\t  |")
        print("-" * 27)

    def h_transaksi(self):
        print("-" * 50)
        print("\t\t  TRANSAKSI")
        print("-" * 50)
        print("| ID   | K_JUS |  N_JUS   | HARGA   | J_ORDER    |")
        print("-" * 50)

    def h_pembayaran(self):
        print("-" * 50)
        print("\t\t  PEMBAYARAN")
        print("-" * 50)
        print("1.NON TUNAI")
        print("2.TUNAI")
        print("-" * 50)

    def h_menu(self):
        c = """ d[-_-]b"""
        result = pyfiglet.figlet_format("MR JUICE", font="cosmic")
        print("=" * 73)
        print(" ")
        print(result)
        print("\t\t\t\t\t\tBy : Rifky Azis", c)
        print("=" * 73)
        print("\t\t\t\t 1. Admin ")
        print("\t\t\t\t 2. Customer ")
        print("\t\t\t\t 0. Keluar")


#print(m)
# menu = Menu()
# menu.h_menu()



