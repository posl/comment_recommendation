def processQuery(A, x, k):
    count = 0
    for i in range(len(A)):
        if A[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1

if __name__ == '__main__':
    processQuery()