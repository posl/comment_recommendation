def main():
    n, m = map(int, input().split())
    divisors = []
    for k in range(1, int(m**0.5)+1):
        if m % k == 0:
            divisors.append(k)
            if k != m//k:
                divisors.append(m//k)
    divisors.sort()
    ans = 0
    for d in divisors:
        if d > m//n:
            break
        if m % d == 0:
            ans += pow(2, n-1, 10**9+7)
    print(ans % (10**9+7))

if __name__ == '__main__':
    main()