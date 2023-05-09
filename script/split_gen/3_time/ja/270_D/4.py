def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N+1)
    for i in range(N+1):
        for a in A:
            if i + a > N:
                break
            if dp[i+a] == 0:
                dp[i] = 1
    if dp[N] == 1:
        print('Takahashi')
    else:
        print('Aoki')
