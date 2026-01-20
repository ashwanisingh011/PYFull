tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)

print(tea_varities[0])

print(tea_varities[-1])

print(tea_varities[1:3])

tea_varities[3] = "Herbal"
print(tea_varities)

tea_varities[1:2] = "Lemon"
print(tea_varities) 

tea_varities[1:2] = ["Lemon"]
print(tea_varities)

for tea in tea_varities:
    print(tea, end="-")


# print()print(len(tea_varities)) 
print(len(tea_varities))

print(tea_varities.count("White"))

print(tea_varities.index("Lemon"))
tea_varities.append("Chamomile")
print(tea_varities)
tea_varities.insert(2, "Earl Grey")
print(tea_varities)