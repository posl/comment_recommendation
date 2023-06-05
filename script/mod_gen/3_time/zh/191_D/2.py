def solve(x, y, r):
    x1 = int(x*10000)
    y1 = int(y*10000)
    r1 = int(r*10000)
    ans = 0
    for i in range(x1-r1, x1+r1+1):
        for j in range(y1-r1, y1+r1+1):
            if (i-x1)*(i-x1) + (j-y1)*(j-y1) <= r1*r1:
                ans += 1
    return ans

if __name__ == '__main__':
    solve()