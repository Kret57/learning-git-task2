from collections import defaultdict
import os
os.system('clear')
shoping_list=defaultdict(list)
i=1
print("Program tworzy liste zakopow")
print("Podaj nazwe sklepu, pozniej produkty z tego sklepu")
print("Nacisnij 'x' aby zakonczyc dodawanie lub sklepow")
while True:
   
    sklep = input(f"Sklep({i}): ").strip()
    if sklep.lower()=="x":
        break
    i+=1
    j=1
    while True:
        produkty=[]
        
        produkt = input(f"Produkt({j}): ")
        if produkt.lower()=="x":
            break
        produkty+=[produkt]
        j+=1
        shoping_list[sklep].extend(produkty)

number_of_items = 0
print()
print("Lista zakupow:")
for shop, items in shoping_list.items():
    Shop=shop.capitalize()
    Item=[item.capitalize() for item in items]
    number_of_items+=len(items)
    print(f"Ide do {Shop} i kupije tam {' '.join(Item)}")
print()
print(f"W sumie kupuje {number_of_items} produktow")