def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        return -1
    ans = 0
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            return -1
        elif A[i+1] - A[i] == 1:
            ans += 1
        else:
            ans += A[i+1]
    return ans
