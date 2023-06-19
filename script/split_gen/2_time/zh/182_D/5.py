def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans = max(ans, sum(a[:i+1]))
    print(ans)
