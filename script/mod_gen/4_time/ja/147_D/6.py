def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    n = 3
    a = [1, 2, 3]
    # n = 10
    # a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    # n = 10
    # a = [3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939, 9375105820]
    # n = 300000
    # a = [1] * 300000
    # print(a)
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(60):
        one = 0
        for j in range(n):
            if a[j] & (1 << i):
                one += 1
        ans += (one * (n - one) * (1 << i))
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()