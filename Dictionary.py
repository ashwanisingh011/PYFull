chai_types = {"Masala": "Spicy",
              "Ginger": "Zesty",
              "Green" : "Mild"
              }

print(chai_types)

chai_types["Green"] = "Fresh"

print(chai_types) 

tea_shop = {
    "chai":{"Masala":  "Spicy", "Ginger": "Zesty"},
    "Tea":{"Green" : "Mild", "Black": "Strong"}
}

print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])