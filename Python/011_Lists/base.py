import random
thislist = ["why dont eggs tell jokes, Cause they'd crack up","why was the pig hired at the resturant, cause he was good at bacon","what do you call a pig that does karate, Porkchop","how do you make a tissue dance, you put a little boogie in it","why did the photo go to jail, cause it was framed"]
rand = random.randrange(0,4)
print(rand)
if rand == 0:
    print(thislist[0])
elif rand == 1:
    print(thislist[1])
elif rand == 2:
    print(thislist[2])
elif rand == 3:
    print(thislist[3])
elif rand == 4:
    print(thislist[4])