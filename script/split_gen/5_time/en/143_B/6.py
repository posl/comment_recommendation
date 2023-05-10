def takoyaki_festival(N, d):
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            result += d[i] * d[j]
    return result
