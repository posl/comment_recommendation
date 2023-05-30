def solution():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    i = 0
    j = 0
    sum = 0
    while sum <= K and (i < N or j < M):
        if i < N and j < M:
            if A[i] < B[j]:
                i += 1
                sum += A[i-1]
            else:
                j += 1
                sum += B[j-1]
        elif i < N:
            i += 1
            sum += A[i-1]
        elif j < M:
            j += 1
            sum += B[j-1]
        if sum <= K:
            ans += 1
    print(ans)
solution()
