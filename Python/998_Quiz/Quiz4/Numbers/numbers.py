mynumbers = [6,9,32,28,15,22,3,18]
highest = 0
for number in mynumbers:
    if number>highest:
        highest = number
print(highest)

bottom = 100
for i in mynumbers:
    if i < bottom:
        bottom = i
print(bottom)

a = 0

for i in mynumbers:
    a+=i
average = a / float(len(mynumbers))
print(average)

    