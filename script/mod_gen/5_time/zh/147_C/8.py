def getNumOfHonestPeople(n, statements):
    honestPeople = 0
    for i in range(1, n + 1):
        honestFlag = True
        for j in range(1, n + 1):
            if i in statements[j]:
                if statements[j][0] == i and statements[j][1] == 1:
                    continue
                else:
                    honestFlag = False
                    break
        if honestFlag:
            honestPeople += 1
    return honestPeople

if __name__ == '__main__':
    getNumOfHonestPeople()