def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p_sum = [0] * (N+1)
    for i in range(N):
        p_sum[i+1] = p_sum[i] + p[i]
    max_sum = 0
    for i in range(N-K+1):
        sum = p_sum[i+K] - p_sum[i]
        if sum > max_sum:
            max_sum = sum
    print((max_sum + K)/2)

if __name__ == '__main__':
    main()