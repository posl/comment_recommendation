def min_health(N, A):
    A.sort()
    for i in range(N-1):
        A[i+1] = A[i+1] % A[i]
    return A[N-1]

if __name__ == '__main__':
    min_health()