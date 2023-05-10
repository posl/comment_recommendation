def main():
  n = int(input())
  a = list(map(int, input().split()))
  ans = [0] * n
  for i in range(n):
    ans[i] = a[i]
  for i in range(1, n):
    if ans[i-1] == a[i]:
      ans[i] = 0
      ans[i-1] = 0
  ans = [i for i in ans if i != 0]
  print(len(ans))
