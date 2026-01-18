name = "Ashwani Singh"
first_char = name[0]
print(first_char)

slice_firstName = name[0 : 7]
print(slice_firstName)


print(name.lower())
print(name.upper())

name2 = "  Ashwani  "
print(name2)
print(name2.strip())

chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))

finder = "Masala Chai"
print(finder.find("Chai"))

girl_type = "Russian"
quantity = 2

order = "I ordered  {} {} girls from Blinkit."
print(order.format(quantity, girl_type) )