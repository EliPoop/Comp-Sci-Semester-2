import random
mylist = ['mcdonalds', 'samvels toes', 'bens toes']
x = random.choice(mylist)
print (x)

mclist = ['nuggets','fries','drink']
samlist = ['big toe','pinky toe','toe pics']
benlist = ['middle toe','broken toe','cheesey toes']



if x == 'mcdonalds':
    y = random.choice(mclist)
    print(y)
elif x == 'samvels toes':
    v = random.choice(samlist)
    print(v)
elif x  == 'bens toes':
    j = random.choice(benlist)
    print(j)
    
    