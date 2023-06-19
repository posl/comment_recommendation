def main():
    a, n = map(int, input().split())
    if n % a != 0:
        print(-1)
        return
    ans = 0
    while n > 1:
        if n % a != 0:
            n -= 1
            ans += 1
        else:
            n //= a
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()