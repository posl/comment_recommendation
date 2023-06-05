def printSequence(n, m):
    if n == 0:
        return [[]]
    elif n == 1:
        return [[i] for i in range(1, m+1)]
    else:
        result = []
        for i in range(1, m+1):
            for j in printSequence(n-1, i):
                result.append([i]+j)
        return result

if __name__ == '__main__':
    printSequence()