import os
os.system('clear')
shoping_list={
    "piekarnia":["chleb","bulki","paczka"],
    "warzywniak":["marchew","seler","rukole"]
}
number_of_items = 0
print("Lista zakupow")
for shop, items in shoping_list.items():
    Shop=shop.capitalize()
    Item=[item.capitalize() for item in items]
    number_of_items+=len(items)
    print(f"Ide do {Shop} i kupije tam {' '.join(Item)}")
print(f"W sumie kupuje {number_of_items} produktow") 