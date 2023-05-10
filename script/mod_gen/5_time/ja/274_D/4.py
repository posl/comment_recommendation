def check(x, y, A):
    n = len(A)
    #print(n)
    for i in range(n):
        #print(i)
        if A[i] == 0:
            return False
        if i == 0:
            if A[i] != abs(x):
                return False
        elif i == n-1:
            if A[i] != abs(y):
                return False
        else:
            if A[i] != abs(x-y):
                return False
    return True

if __name__ == '__main__':
    check()