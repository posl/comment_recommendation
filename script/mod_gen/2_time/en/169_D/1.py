def main():
    n = int(input())
    i = 2
    ans = 0
    while i*i <= n:
        while n % i == 0:
            n //= i
            ans += 1
        i += 1
    if n > 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()