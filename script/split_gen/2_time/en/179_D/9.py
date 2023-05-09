def main():
  import sys
  readline = sys.stdin.readline
  N, K = map(int, readline().split())
  LR = [list(map(int, readline().split())) for _ in range(K)]
  LR.sort()
  MOD = 998244353
  dp = [0] * (N + 1)
  dp[1] = 1
  for i in range(N):
    for l, r in LR:
      if i + l > N:
        break
      dp[i + l] += dp[i]
      dp[i + l] %= MOD
      if i + r + 1 <= N:
        dp[i + r + 1] -= dp[i]
        dp[i + r + 1] %= MOD
  for i in range(1, N + 1):
    dp[i] += dp[i - 1]
    dp[i] %= MOD
  print(dp[N])
