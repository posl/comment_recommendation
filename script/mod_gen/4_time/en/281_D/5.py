def solve():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if K > N:
        return -1
    if D == 1:
        return A[0]
    for i in range(N):
        if i + K > N:
            break
        if A[i] % D == 0:
            return A[i]
    return -1
print(solve())
