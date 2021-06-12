Number = []

while True:
    tmp = int(input("정수입력(0=종료, 검색하려면 -를 붙이세요.)":))
    if tmp ==0:
        break
    # 저장
    if tmp > 0:
        if len(Number) ==0:
            Number.append(tmp)
        else:
            for i, v in enumerate(Number):
                if tmp == v:
                    print("중복값이 있습니다.")
                    continue
                if tmp < v:
                    Number.insert(i, tmp)
                    break
                if i == len(Number)-1:
                    Number.append(tmp)
                    break
        print(Number)
        print("총 {}개의 정수가 저장되었습니다.".format(len(Number)))
        else:
            lookup = -tmp
            start = 0
            end = len(Number) - 1
            key = int((start + end) / 2)
            while True:
                if start > end:
                    print("찾는 값이 없습니다.")
                    break
                if Number[key] == lookup:
                    print("{}(은)는 {}번째 위치에 있습니다.".format(lookup, key))
                    break
                elif Number[key] < lookup:
                    start = key + 1
                    key = int((start + end) / 2 )
                else:
                    end = key - 1
                    key = int((start + end) / 2 )
