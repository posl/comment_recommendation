def main():
  # n, m = map(int, input().split())
  # s = [list(input()) for _ in range(n)]
  n, m = 5, 5
  s = [['o','o','o','o','o'],['o','o','o','x','x'],['x','x','o','o','o'],['o','x','o','x','o'],['x','x','x','x','x']]
  ans = 0
  for i in range(n):
    for j in range(i+1,n):
      count = 0
      for k in range(m):
        if s[i][k] == 'o' or s[j][k] == 'o':
          count += 1
      if count == m:
        ans += 1
  print(ans)
