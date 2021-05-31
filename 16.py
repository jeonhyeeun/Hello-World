test = [90, 25, 67, 45, 80]

number = 0
for test in test:
    number = number + 1
    if test >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불학격 입니다." % number)
