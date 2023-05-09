def solve():
  n, m = map(int, input().split())
  a = [0] * m
  b = [0] * m
  for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
  ans = [-1] * n
  ans[0] = 0
  for i in range(m):
    if ans[a[i]] == -1:
      ans[a[i]] = ans[b[i]]
    elif ans[b[i]] == -1:
      ans[b[i]] = ans[a[i]]
    else:
      if ans[a[i]] == ans[b[i]]:
        print(-1)
        return
      else:
        if ans[a[i]] == 0:
          ans[b[i]] = 1
        else:
          ans[b[i]] = 0
  for i in range(n):
    if ans[i] == -1:
      ans[i] = 0
  ans = [x + 1 for x in ans]
  print(*ans)
  return
