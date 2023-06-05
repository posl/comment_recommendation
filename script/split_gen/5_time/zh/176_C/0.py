def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    max_h = 0
    ans = 0
    for i in range(N):
        if max_h <= A[i]:
            ans += A[i] - max_h
            max_h = A[i]
        else:
            max_h = A[i]
    print(ans)
