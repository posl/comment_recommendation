def main():
    N = int(input())
    # N = 100000
    N += 1
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        n = N
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt == 1:
            ans -= 1
        while n % i == 0:
            n //= i
        if n == 1:
            continue
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                ans -= 1
                break
    print(ans)

if __name__ == '__main__':
    main()