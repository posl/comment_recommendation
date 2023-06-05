def findMinTimes(A):
    A = sorted(A)
    count = 0
    for i in range(len(A)):
        if i == 0:
            count += A[i]
        else:
            if A[i] == A[i-1]:
                count += A[i] + 1
            else:
                count += A[i] - A[i-1] + 1
    return count

if __name__ == '__main__':
    findMinTimes()