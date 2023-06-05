def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    for i in range(1, n + 1):
        p[i] += p[i - 1]
    ans = 0
    for i in range(k, n + 1):
        ans = max(ans, p[i] - p[i - k])
    print((ans + k) / 2)

if __name__ == '__main__':
    main()