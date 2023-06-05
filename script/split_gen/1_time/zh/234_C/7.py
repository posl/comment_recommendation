def findKthNumber(k):
    if k <= 2:
        return 2*k
    else:
        k = k-2
        cnt = 0
        i = 2
        while True:
            if i % 10 == 0:
                i += 2
                continue
            if i % 10 == 2:
                cnt += 1
                if cnt == k:
                    return i
            i += 2
