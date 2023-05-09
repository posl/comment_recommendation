def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2**N+1)
    for i in range(1, N+1):
        ans[2*i] = ans[A[i-1]] + 1
        ans[2*i+1] = ans[A[i-1]] + 1
    for i in range(1, 2**N+1):
        print(ans[i])
