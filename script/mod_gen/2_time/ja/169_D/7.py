def main():
    N = int(input())
    ans = 0
    for p in range(2, 100000):
        if p*p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            N //= p
            e += 1
        ans += e
    if N > 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()