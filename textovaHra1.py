import os

store_items = ["potion","sword","armor","shield"]
store_items_prices = [10,5,13,17]

def clear():
    os.system("cls")


def vypisObchodCeny():
    for i in range(len(store_items)):
        print(f"  {i+1}. {store_items[i]}\t{store_items_prices[i]}")

# TODO: 
# nize mas seznam itemu, ktere nabizi obchod a pod nim seznam jejich cen ve stejnem poradi

# tvuj inventar a seznam cen predmetu v tvem inventari (zatim nic nemas)
inventory = []
inventory_prices = []

# pocet penez, ktere mas k dispozici
money = 15


vypisObchodCeny()
nakup = int(input("co chces?"))-1
inventory.append(store_items[nakup])
money -= store_items_prices[nakup]

clear()

print(inventory)
print(f"tvoje prachy: {money}")
vypisObchodCeny()

# TODO: vypis vsechny predmety, ktere obchod nabizi a jejich ceny
# Items in store: 
#   1. potion     10
#   2. sword      5
#   3. armor      13
#   4. shield     17


# TODO: nech uzivatele zvolit poradi predmetu, ktery chce koupit a pridej mu ten predmet do inventare
# POZOR: predmet lze koupit pouze pokud ma hrac dost penez



# TODO: pridej i moznost buy a sell
# 1. zeptej se uzivatele, zda chce kupovat nebo prodavat
# 2. podle jeho volby:
    # pokud si zvolil nakup -> zobraz seznam predmetu v obchode
    #   ...          prodej -> zobraz seznam predmetu z inventare

    

# BONUS2 TODO: pridej moznost nechat si vypsat celkovou hodnotu vsech veci ve tvem inventari





