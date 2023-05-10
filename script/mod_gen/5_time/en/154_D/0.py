def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = [0] * (N + 1)
    for i in range(N):
        p_sum[i + 1] = p_sum[i] + p[i]
    max_exp = 0
    for i in range(N - K + 1):
        exp = (p_sum[i + K] - p_sum[i]) / 2 + p_sum[i]
        if exp > max_exp:
            max_exp = exp
    print(max_exp)

if __name__ == '__main__':
    main()