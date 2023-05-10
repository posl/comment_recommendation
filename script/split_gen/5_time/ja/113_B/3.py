def main():
  n = int(input())
  t, a = map(int, input().split())
  h = list(map(int, input().split()))
  ans = 0
  ans_diff = 1000000000
  for i in range(n):
    diff = abs(a-(t-h[i]*0.006))
    if ans_diff > diff:
      ans_diff = diff
      ans = i+1
  print(ans)
