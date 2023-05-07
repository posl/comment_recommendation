def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        n1 = 0
        for j in range(n):
            if a[j] & (1 << i):
                n1 += 1
        ans += (n1 * (n - n1) * (1 << i))
    print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    main()