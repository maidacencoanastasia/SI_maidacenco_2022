'''
print("Maidacenco Anastasia")

numele = "Maidacenco Anastasia"

def salutare(numele):
    return ("Hello, "+numele+"!")
print(salutare(numele))

#Some changes
name = input("What is you name? ")
if name == "Adela":
    print("Greetengs Ms "+name+"! "+"I hope you are doing well!")
else:
    print(salutare(name))
'''
# dictionar
inventar = {"scaune":33,"mese":22,"tabla":1}
res = list(inventar.values())
print(sum(res))
print(res)
