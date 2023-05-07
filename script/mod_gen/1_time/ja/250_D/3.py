def main():
    N = int(input())
    ans = 0
    p = 2
    while p * p * p <= N:
        q = 2
        while p * q * q * q <= N:
            ans += 1
            q += 1
        p += 1
    print(ans)

if __name__ == '__main__':
    main()