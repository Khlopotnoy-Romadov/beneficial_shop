from main import shops
print(shops)
print()

def list_of_purchases(lst: list)->list:
    values = dict()
    for i in lst:
        for j in shops.keys():
            if j in values.keys():
                values[j] += shops[j][i]
            else:
                values[j] = shops[j][i]
    print(values)
    min = 10000000
    min_mag = ""
    for i in values.keys():
        if values[i]<min:
            min = values[i]
            min_mag = i
    return [min_mag, shops[min_mag]['адрес']]

print(list_of_purchases(["колбаса", "огурцы"]))







