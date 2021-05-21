total = 0
counter = 1
while counter <= 10:
    grade=int(input("Enter grde: "))
    total = grade + total
    counter = counter + 1
average = total / 10
print(average)
