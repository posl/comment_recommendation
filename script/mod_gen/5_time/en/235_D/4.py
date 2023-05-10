def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 1:
        print(n-1)
        return
    ans = 0
    while n > 1:
        if n % a == 0:
            n = n // a
        else:
            n -= 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()