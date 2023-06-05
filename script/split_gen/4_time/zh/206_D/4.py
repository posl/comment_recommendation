def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += 1
    print(ans)
