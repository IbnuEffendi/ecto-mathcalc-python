#MODULE AKAR
#import math 
#a = math.sqrt(4) #AKAR KUADRAT
#b = math.pow(16.0,1/4.0) #AKAR PANGKAT 3++
#print (a)
#print (b) 
from time import *
import math

    
    
def menu():
    print ("___________________________________")
    print ("\                                 |")
    print (" |  MENU                          |")
    print (" |   1) LINGKARAN                 |")
    print (" |   2) QUIT                      |")
    print (" |  Pilih dengan mengetik angka   |")
    print (" |________________________________|")
    menu = input(">> ")
    if menu in "1":
       lingkaran()
    elif menu in "2":
       quit()
    else: 
       loop_a()
       
def loop_a():
    print ("___________________________________")
    print ("\                                 |")
    print (" |  Pilih Dengan Mengetik Angka!  |")
    print (" |________________________________|")
    menu = input(">> ")       
    if menu in "1":
       sleep(1)
       lingkaran()
    elif menu in "2":
       sleep(1)
       quit()
    else: 
       loop_a()

def quit():
    print ("__________________________ ")
    print ("\                        |")
    print (" | QUITING PROGRAM . . . |")
    print (" |_______________________|")
    sleep(2)
    print ("________________")
    print ("\              |")
    print (" |  GOOD BYE!  |")
    print (" |_____________|")
    
def lingkaran():
    print ("__________________")
    print ("\                |")
    print (" | PILIH RUMUS!  |")
    print (" |  1) LUAS      |")
    print (" |  2) KELILING  |")
    print (" |_______________|")
    piliha = input(">> ")
    if piliha in "1":
         sleep(1)
         lingkaran_a()
    elif piliha in "2":
         sleep(1)
         lingkaran_b()
    else:
         sleep(1)
         loop_b()

def lingkaran_b():
    print ("_____________________________________")
    print ("\                                   |")
    print (" | MASIH DALAM PROSES PENGEMBANGAN! |")
    print (" |__________________________________|")
    sleep(1)
    lingkaran()
  
  
  

def loop_b():
    print ("___________________________________")
    print ("\                                 |")
    print (" |  Pilih Dengan Mengetik Angka!  |")
    print (" |________________________________|")
    menu = input(">> ")       
    if menu in "1":
       sleep(1)
       lingkaran_a()
    elif menu in "2":
       sleep(1)
       lingkaran_b()
    else: 
       loop_b()

        
def lingkaran_a():
         print ("__________________________")
         print ("\                        |")
         print (" |  APA YANG DIKETAHUI?  |")
         print (" |    1) Diameter (d)    |")
         print (" |    2) Jari-Jari (r)   |")
         print (" |_______________________|")
         pilih = input(">> ")
         if pilih in "1":
            diameter()
         elif pilih in "2":
              jari()
         else:
           loop_d
     
def loop_d():
    print ("___________________________________")
    print ("\                                 |")
    print (" |  Pilih Dengan Mengetik Angka!  |")
    print (" |________________________________|")
    menu_a = input(">> ")       
    if menu_a in "1":
       sleep(1)
       diameter()
    elif menu_a in "2":
       sleep(1)
       jari()
    else: 
       loop_d()
      
      
       
def diameter():
    pi = 3.14
    pia = 22
    pib = 7
    print ("_____________________________")
    print ("\                           |")
    print (" |    Masukkan Diameter!    |")
    print (" |__________________________|")
    d = int(input(">> "))
    r = d / 2
    sleep(1)
    print ("_____________________________")
    print ("\                           |")
    print (" |    CALCULATING . . .     |")
    print (" |__________________________|")
    sleep(2)
    if r % pib == 0:
       hasil = r * r / pib * pia
       print ("________________________")
       print ("\                      |")
       print (" |  JAWABAN            |")
       print (" |    L =",hasil)
       print (" |_____________________|")
       sleep(1)
       print ("______________________________________________________________")
       print ("\                      ")
       sleep(1)
       print (" | CARA PENGERJAAN")
       sleep(1)
       print (" |   L = π x (d : 2) x (d : 2)")
       sleep(1)
       print (" |   L = 22/7 x (",d," : 2) x (",d," : 2)")
       sleep(1)
       print (" |   L = 22/7 x ", r," x ", r)
       sleep(1)
       print (" |   L = 22/1 x ", r / pib, " x ", r)
       sleep(1)
       print (" |   L =",hasil)
       sleep(1)
       print (" |____________________________________________________________")
       loop_e()
    else:
       hasil = pi * r * r 
       print ("________________________")
       print ("\                      |")
       print (" |  JAWABAN            |")
       print (" |    L =",hasil)
       print (" |_____________________|")
       sleep(1)
       print ("______________________________________________________________")
       print ("\                      ")
       sleep(1)
       print (" | CARA PENGERJAAN")
       sleep(1)
       print (" |   L = π x (d : 2) x (d : 2)")
       sleep(1)
       print (" |   L = 3,14 x (",d," : ",2,") x (",d," : ",2,")")
       sleep(1)
       print (" |   L = 3,14 x ",r," x ",r)
       sleep(1)
       print (" |   L = 3,14 x ",r*r)
       sleep(1)
       print (" |   L =",hasil)
       sleep(1)
       print (" |____________________________________________________________") 
       loop_e()
       
       
def jari():
    pi = 3.14
    pia = 22
    pib = 7
    print ("_____________________________")
    print ("\                           |")
    print (" |   Masukkan Jari-Jari!    |")
    print (" |__________________________|")
    r = int(input(">> "))
    sleep(1)
    print ("_____________________________")
    print ("\                           |")
    print (" |    CALCULATING . . .     |")
    print (" |__________________________|")
    sleep(2)
    if r % pib == 0:
       hasil = r * r / pib * pia
       print ("________________________")
       print ("\                      |")
       print (" |  JAWABAN            |")
       print (" |    L =",hasil)
       print (" |_____________________|")
       sleep(1)
       print ("______________________________________________________________")
       print ("\                      ")
       sleep(1)
       print (" | CARA PENGERJAAN")
       sleep(1)
       print (" |   L = π x r x r")
       sleep(1)
       print (" |   L = 22/7 x ", r," x ", r)
       sleep(1)
       print (" |   L = 22/1 x ", r / pib, " x ", r)
       sleep(1)
       print (" |   L = 22/1 x ", r/pib*r)
       sleep(1)
       print (" |   L =",hasil)
       sleep(1)
       print (" |____________________________________________________________")
       loop_e()
    else:
       hasil = pi * r * r 
       print ("________________________")
       print ("\                      |")
       print (" |  JAWABAN            |")
       print (" |    L =",hasil)
       print (" |_____________________|")
       sleep(1)
       print ("______________________________________________________________")
       print ("\                      ")
       sleep(1)
       print (" | CARA PENGERJAAN")
       sleep(1)
       print (" |   L = π x r x r")
       sleep(1)
       print (" |   L = 3,14 x ",r,"x",r)
       sleep(1)
       print (" |   L = 3,14 x ",r*r)
       sleep(1)
       print (" |   L =",hasil)
       sleep(1)
       print (" |____________________________________________________________")
       loop_e()
       
       
       
       
def loop_e():
    sleep(2)
    print ("___________________________________")
    print ("\                                 |")
    print (" |  Ingin Menghitung Ulang?(y/n)  |")
    print (" |________________________________|")
    menu_a = input(">> ")       
    if menu_a in "y":
       sleep(1)
       lingkaran_a()
    elif menu_a in "n":
       sleep(1)
       menu()
    else: 
       loop_e()


def starting():
    print ("_____________________________")
    print ("\                           |")
    print (" |  STARTING PROGRAM . . .  |")
    print (" |__________________________|")
    sleep(2)
    menu()
       
       
       
def kenalan():
    print ("______________________________________")
    print ("\                                    |")
    print (" |  Halo! Aku Ecto, Siap Membantumu  |")
    print (" |___________________________________|")
    print ("")
    sleep(2)
    print ("_______________________________________")
    print ("\                                     |")
    print (" | Saat ini aku baru bisa mengerjakan |")
    print (" | rumus luas lingkaran. Aku akan     |")
    print (" | menjawab pertanyaanmu dengan benar |")
    print (" | dan lengkap dengan cara            | ")
    print (" | pengerjaannya.                     |")
    print (" |____________________________________|")
    print ("")
    sleep(5)
    print ("_______________________________________")
    print ("\                                     |")
    print (" | Apakah Anda Ingin Mencobanya?(y/n) |")
    print (" |____________________________________|")
    menu_a = input(">> ")
    if menu_a in "y":
       starting()
    elif menu_a in "n":
       quit()
    else: 
       loop_c()
      
      
def loop_c():
    print ("___________________________________")
    print ("\                                 |")
    print (" |  Pilih Dengan Mengetik y/n!    |")
    print (" |________________________________|")
    menu_a = input(">> ")       
    if menu_a in "y":
       sleep(1)
       starting()       
    elif menu_a in "n":
       sleep(1)
       quit()
    else: 
       loop_c()
    
       
kenalan()