def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    sum_p = [0] * (N+1)
    for i in range(1, N+1):
        sum_p[i] = sum_p[i-1] + p[i]
    ans = 0
    for i in range(1, N-K+2):
        ans = max(ans, (sum_p[i+K-1] - sum_p[i-1])/K)
    print(ans)

if __name__ == '__main__':
    main()