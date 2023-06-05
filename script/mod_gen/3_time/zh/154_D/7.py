def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = [0] * (n + 1)
    for i in range(n):
        p_sum[i + 1] = p_sum[i] + p[i]
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, (p_sum[i + k] - p_sum[i]) / 2 + p_sum[i])
    print(ans)

if __name__ == '__main__':
    main()