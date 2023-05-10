def main():
  S = input()
  S_len = len(S)
  chokudai = "chokudai"
  chokudai_len = len(chokudai)
  dp = [[0 for _ in range(chokudai_len+1)] for _ in range(S_len+1)]
  dp[0][0] = 1
  for i in range(S_len):
    for j in range(chokudai_len+1):
      dp[i+1][j] += dp[i][j]
      if j < chokudai_len and S[i] == chokudai[j]:
        dp[i+1][j+1] += dp[i][j]
    for j in range(chokudai_len+1):
      dp[i+1][j] %= 10**9 + 7
  print(dp[S_len][chokudai_len])
