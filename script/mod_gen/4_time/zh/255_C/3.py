def main():
    x, a, d, n = map(int, input().split())
    ans = 0
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    elif d > 0:
        while x < a:
            x += 1
            ans += 1
        while x > a + d * (n - 1):
            x -= 1
            ans += 1
        print(ans)
    else:
        while x > a:
            x -= 1
            ans += 1
        while x < a + d * (n - 1):
            x += 1
            ans += 1
        print(ans)

if __name__ == '__main__':
    main()