def solve():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            ans += int(x)
        else:
            ans += float(x) * 380000
    print(ans)
solve()
