def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(n // 2):
        ans += A[2 * i + 1] - A[2 * i]
    print(ans)
solve()
