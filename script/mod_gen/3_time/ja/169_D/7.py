def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    p = 2
    ans = 0
    while p * p <= N:
        e = 1
        while N % p == 0:
            N //= p
            e += 1
        ans += e - 1
        p += 1
    if N > 1:
        ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()