def main():
  n, k = map(int, input().split())
  p = list(map(int, input().split()))
  p = [0] + p
  s = [0] * (n + 1)
  for i in range(1, n + 1):
    s[i] = s[i - 1] + p[i]
  t = 0
  for i in range(n - k + 1):
    t = max(t, (s[i + k] - s[i]) / 2 + s[i])
  print(t)
