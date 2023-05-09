def solve(n, a):
  ans = 0
  for i in range(n):
    ans += (n - 1) * a[i] ** 2
  for i in range(n - 1):
    ans -= 2 * (n - i - 1) * a[i] * sum(a[i + 1:])
  return ans
