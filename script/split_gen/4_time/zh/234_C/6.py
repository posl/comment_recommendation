def getKthNumber(k):
    if k == 1:
        return 2
    elif k == 2:
        return 20
    elif k == 3:
        return 22
    else:
        return 20 * (10**(k-3)) + getKthNumber(k-2)
k = int(input())
print(getKthNumber(k))
