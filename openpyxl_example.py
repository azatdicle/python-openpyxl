import openpyxl
import sys
from colorama import init, Fore
print(Fore.GREEN +"""
 __   ___       _______   __
 \ \ / / |     / ____\ \ / /
  \ V /| |    | (___  \ V / 
   > < | |     \___ \  > <  
  / . \| |____ ____) |/ . \ 
 /_/ \_\______|_____//_/ \_\'
                            
        @azatdicle                                                       
      """+Fore.RESET)

def xlsx():
    dosya = openpyxl.load_workbook("car_brands_and_models.xlsx")
    dosyaac = dosya.active
    listem = []
    sayac = 0
    
    for cell_b, cell_c in zip(dosyaac['A'], dosyaac['B']):
        if cell_b.value is None and cell_c.value is None:
            pass
        else:
            listem.append((sayac, cell_b.value, "|", cell_c.value))
            sayac += 1
            
    return listem  

listem = xlsx()  
uzunluk = len(listem) 

while True:
    print("More query,all_car")
    sorgu = input("Which car brand are you looking for?: ")
    if sorgu=="all_car":
        for x in listem:
            print(x)
    if sorgu == "Exit"  :
        sys.exit()
        print("Bye Bye............. :)")
    found = False  
    for x in range(uzunluk):
        if listem[x][1] == sorgu:
            print(Fore.YELLOW + str(listem[x][1:4]) + Fore.RESET)
            found = True  
   
    if not found:
        print(Fore.RED+"car not found."+Fore.RESET)
    print("-----------------------------------")
