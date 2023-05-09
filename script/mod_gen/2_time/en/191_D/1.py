def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    ans = 0
    for i in range(int(x - r), int(x + r) + 1):
        if i < 0:
            continue
        if i > 10 ** 5:
            break
        a = (r ** 2 - (i - x) ** 2) ** 0.5
        ans += int(y + a) - int(y - a) + 1
    print(ans)

if __name__ == '__main__':
    main()