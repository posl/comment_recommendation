def main():
    import math
    x, y, r = map(float, input().split())
    x = int(x * 10**4)
    y = int(y * 10**4)
    r = int(r * 10**4)
    ans = 0
    for i in range(x - r, x + r + 1):
        if i % 10**4 != 0:
            continue
        y_range = r**2 - (i - x)**2
        y_range = math.floor(math.sqrt(y_range))
        y_min = y - y_range
        y_max = y + y_range
        y_min = math.ceil(y_min / 10**4) * 10**4
        y_max = math.floor(y_max / 10**4) * 10**4
        ans += (y_max - y_min) // 10**4 + 1
    print(ans)

if __name__ == '__main__':
    main()