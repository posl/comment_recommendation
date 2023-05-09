def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    for i in range(1, n + 1):
        p[i] += p[i - 1]
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, (p[i + k] - p[i]) / 2 + p[i])
    print(ans)
main()

if __name__ == '__main__':
    main()