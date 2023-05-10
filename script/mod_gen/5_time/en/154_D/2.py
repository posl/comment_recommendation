def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = [0]
    for i in range(n):
        p_sum.append(p_sum[i] + p[i])
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, p_sum[i + k] - p_sum[i])
    print((ans + k) / 2)

if __name__ == '__main__':
    main()