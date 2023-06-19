def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    for i in range(N):
        sum += A[i]
        ans = max(ans, sum)
    print(ans)
solve()
