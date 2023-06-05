def main():
    n = int(input())
    a = 2
    b = 2
    ans = 0
    while a**b <= n:
        while a**b <= n:
            ans += 1
            b += 1
        a += 1
        b = 2
    print(n - ans)

if __name__ == '__main__':
    main()