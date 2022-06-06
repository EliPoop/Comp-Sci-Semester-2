items = int(input("how many items "))

total = 0
for i in range(0,items):
    name = input("whats the item")
    price = int(input("whats the price"))
    print("thanks for buying" + name)
    total = total + price

print("your total is: " + str(total))

    
    
