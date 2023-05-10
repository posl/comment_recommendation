def getNumOfGeneration(N, P):
    result = 0
    for i in range(1, N):
        if P[i] == 1:
            if result < i:
                result = i
        else:
            result += 1
    return result
