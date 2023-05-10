def main():
    n = int(input())
    ans = 0
    a = 1
    while a <= n:
        b = a
        while b <= n:
            c = b
            while c <= n:
                ans += 1
                c *= 5
            b *= 3
        a *= 2
    print(ans)

if __name__ == '__main__':
    main()