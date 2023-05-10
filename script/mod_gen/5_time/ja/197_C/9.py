def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(2 ** (n - 1)):
        tmp = 0
        xor = 0
        for j in range(n):
            tmp |= a[j]
            if i >> j & 1:
                xor ^= tmp
                tmp = 0
        xor ^= tmp
        ans = min(ans, xor)
    print(ans)

if __name__ == '__main__':
    main()