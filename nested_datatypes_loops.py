food={"vegetables":["carrots","kale","cucumber","tomato"],"desserts":["cake","ice cream", "donut"]}
print("My favorite dessert is " + food["desserts"][0])
print("My favorite dessert is " + food["desserts"][1])

cars={"sports":{"Volkswagon":"Porsche","Dodge":"Viper","Chevy":"Corvette"},"classic":{"Mercedes-Benz":"300SL","Toyota":"2000GT","Lincoln":"Continental"}}
print("My favorite classic car is a " + cars["classic"]["Toyota"])
print("My favorite classic car is a " + cars["classic"]["Lincoln"])

#Parse datatypes with loops
for hungry in food["desserts"]:
    print("My favorite dessert is " + hungry)

for auto in cars["classic"]:
    print("My favorite classic car is a " + cars["classic"][auto])