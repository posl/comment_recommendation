def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000 + 0.5)
    y = int(y * 10000 + 0.5)
    r = int(r * 10000 + 0.5)
    ans = 0
    for i in range(x-r, x+r+1, 10000):
        ans += int((r**2 - (x-i)**2)**0.5 / 10000) * 2 + 1
    print(ans)
