def main():
    a, n = map(int, input().split())
    if a == 1:
        print(n - 1)
        return
    if n % a != 0:
        print(-1)
        return
    n = n // a
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % a == 1:
            n -= 1
            ans += 1
        else:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()