def getNumOfProblems(D, G, p, c):
    minNum = 10000
    for i in range(2**D):
        b = bin(i)[2:].zfill(D)
        totalScore = 0
        num = 0
        for j in range(D):
            if b[j] == '1':
                totalScore += p[j] * (j + 1) * 100 + c[j]
                num += p[j]
        for j in range(D - 1, -1, -1):
            if b[j] == '0':
                if totalScore < G:
                    if totalScore + p[j] * (j + 1) * 100 >= G:
                        num += (G - totalScore) // ((j + 1) * 100)
                break
        if totalScore >= G and num < minNum:
            minNum = num
    return minNum
