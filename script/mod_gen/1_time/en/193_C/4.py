def main():
    n = int(input())
    a = 2
    b = 2
    ans = n-1
    while a <= n:
        while b <= n:
            if a**b <= n:
                ans -= 1
            b += 1
        a += 1
        b = 2
    print(ans)

if __name__ == '__main__':
    main()