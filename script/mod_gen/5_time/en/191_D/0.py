def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    ans = 0
    for i in range(-r, r + 1):
        j = r - abs(i)
        if x - r <= i <= x + r:
            ans += (y + j + 9999) // 10000 - (y - j) // 10000 + 1
    print(ans)

if __name__ == '__main__':
    main()