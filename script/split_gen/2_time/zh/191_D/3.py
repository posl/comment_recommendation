def solve():
    x, y, r = map(float, input().split())
    x, y, r = int(x*10000), int(y*10000), int(r*10000)
    ans = 0
    for i in range(y-r, y+r+1):
        for j in range(x-r, x+r+1):
            if (i-y)**2 + (j-x)**2 <= r**2:
                ans += 1
    print(ans)
solve()
