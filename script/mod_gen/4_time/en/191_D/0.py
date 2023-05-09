def main():
    x, y, r = map(float, input().split())
    x = int(x * 10 ** 4)
    y = int(y * 10 ** 4)
    r = int(r * 10 ** 4)
    ans = 0
    for i in range(x - r, x + r + 1):
        d = (r ** 2 - (i - x) ** 2) ** 0.5
        u = y + d
        l = y - d
        if u % 10000 == 0:
            u -= 1
        if l % 10000 == 0:
            l += 1
        ans += (u // 10000 - l // 10000) + 1
    print(ans)

if __name__ == '__main__':
    main()