def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  if n == 1:
    if a[0] == 1:
      print(0)
    else:
      print(-1)
    return
  if a[0] != 1:
    print(-1)
    return
  ans = 0
  for i in range(1, n):
    if a[i] - a[i - 1] > 1:
      print(-1)
      return
    elif a[i] - a[i - 1] == 1:
      ans += 1
  print(n - ans - 1)
  return

if __name__ == '__main__':
    resolve()