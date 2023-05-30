def problem148_d():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        return -1
    for i in range(1, N):
        if A[i] - A[i-1] > 1:
            return -1
    ans = 0
    for i in range(N-1, 0, -1):
        if A[i] == A[i-1] + 1:
            ans += 1
        else:
            ans += A[i]
    return ans
print(problem148_d())
