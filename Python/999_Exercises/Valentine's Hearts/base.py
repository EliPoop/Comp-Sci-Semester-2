import datetime
compliment_list = []
with open ('compliment_list') as f


with open('People.txt') as f:
    for line in f:
        l = line.strip()
        print(l)

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        print(l)



import random
pnum = random.randrange(0,len(people_list))
cnum = random.randrange(0,len(compliment_list))


x = datetime.datetime.now()

print()
print("The date and time are:")
print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

f.close()
