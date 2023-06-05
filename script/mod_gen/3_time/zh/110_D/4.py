def main():
    n, m = map(int, input().split())
    if m == 1:
        print(1)
        return
    if n == 1:
        print(1)
        return
    prime = []
    for i in range(2, int(m**0.5)+1):
        if m % i == 0:
            prime.append(i)
            while m % i == 0:
                m //= i
    if m != 1:
        prime.append(m)
    ans = 1
    for p in prime:
        cnt = 0
        while m % p == 0:
            m //= p
            cnt += 1
        ans *= cmb(cnt+n-1, n-1)
        ans %= 10**9+7
    print(ans)

if __name__ == '__main__':
    main()