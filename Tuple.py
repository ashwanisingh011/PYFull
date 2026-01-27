tea_types = ("Black", "Green", "Oolong")
print(tea_types)

print(tea_types[0])
print(tea_types[-1])

tea_types[0] = "Lemon" # This will give as error because tuples are immutable we can't change them. 
print(tea_types)