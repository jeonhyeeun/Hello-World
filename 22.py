import random
numList = (1, 5, 7, 13, 50, 120, 300, 320, 400, 700)

for k in range(10):
    number = 0
    for i in range(10000):
        number = numList[random.randint(0, 9)]
        for n in numList:
            number += 1
            if n == number:
                break
    print(number/10000)
