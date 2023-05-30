def max_sum():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    #print(A)
    count = 0
    for i in range(M):
        count += A[i]
    for i in range(M, N):
        if A[i] < 0:
            break
        count += A[i]
    return count
print(max_sum())
