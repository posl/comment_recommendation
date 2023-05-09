def main():
    x, y, n = map(int, input().split())
    ans = 0
    while n > 0:
        if n % 3 == 0:
            ans += (n // 3) * y
            n = 0
        else:
            ans += x
            n -= 1
    print(ans)

if __name__ == '__main__':
    main()