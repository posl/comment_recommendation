def getMinMP(n, a, b, c, l):
    minMP = 10 ** 9
    for i in range(4 ** n):
        tmp = i
        mp = 0
        a1, b1, c1 = 0, 0, 0
        for j in range(n):
            if tmp % 4 == 1:
                a1 += l[j]
                mp += 10
            elif tmp % 4 == 2:
                b1 += l[j]
                mp += 10
            elif tmp % 4 == 3:
                c1 += l[j]
                mp += 10
            tmp //= 4
        if a1 > 0 and b1 > 0 and c1 > 0:
            mp += abs(a - a1) + abs(b - b1) + abs(c - c1)
            minMP = min(mp, minMP)
    return minMP
