def main():
    n = int(input())
    ans = 0
    x = 1
    while x * x <= n:
        if n % x == 0:
            ans = max(ans, x)
            ans = max(ans, n // x)
        x += 1
    print(ans - 2)

if __name__ == '__main__':
    main()