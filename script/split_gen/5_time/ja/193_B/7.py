def solve():
    n = int(input())
    shops = []
    for _ in range(n):
        a, p, x = map(int, input().split())
        shops.append((a, p, x))
    ans = 10**9 + 1
    for a, p, x in shops:
        if x >= 1:
            ans = min(ans, p)
    if ans == 10**9 + 1:
        ans = -1
    print(ans)
