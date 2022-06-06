import random
x = int(input("how many random numbers would you like "))
thislist = [1,2,3,4,5,6,7,8,9,10]

for y in range(0,x):
    z = random.choice(thislist)
    print(z, end= " , ")