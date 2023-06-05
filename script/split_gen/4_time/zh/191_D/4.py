def main():
    x, y, r = map(float, input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    ans = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if (i-x)*(i-x) + (j-y)*(j-y) <= r*r:
                ans += 1
    print(ans)
