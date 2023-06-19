def findmin(A):
    n = len(A)
    if n == 1:
        if A[0] == 0:
            return 1
        else:
            return 0
    else:
        A.sort()
        if A[0] > 0:
            return 0
        else:
            for i in range(1, n):
                if A[i] - A[i - 1] > 1:
                    return A[i - 1] + 1
            return A[n - 1] + 1

if __name__ == '__main__':
    findmin()