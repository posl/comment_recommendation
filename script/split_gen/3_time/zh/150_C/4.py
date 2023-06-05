def getNum(a):
    n = len(a)
    if n == 1:
        return 0
    if n == 2:
        return 1 if a[0] > a[1] else 0
    else:
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if a[i] > a[j]:
                    count += 1
        return count
