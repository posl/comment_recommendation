def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        return -1
    if N == 1:
        return 0
    ans = 0
    for i in range(N - 1):
        if A[i] + 1 == A[i + 1]:
            ans += 1
        elif A[i] < A[i + 1]:
            return -1
        else:
            ans += A[i + 1]
    return ans
print(solve())
