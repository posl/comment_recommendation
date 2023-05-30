def solve():
  n = int(input())
  a = [int(x) for x in input().split()]
  s = sum(a)
  ans = [0] * n
  ans[0] = s
  for i in range(1,n):
    ans[i] = 2 * (a[i-1] - ans[i-1] // 2)
  print(*ans)
solve()
