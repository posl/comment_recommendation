def solve():
  n = int(input())
  a = [int(i) - 1 for i in input().split()]
  b = [0] * (2 * n + 1)
  for i in range(n):
    b[a[i]] = i + 1
  for i in range(2 * n - 1, 0, -1):
    b[i // 2] += b[i]
  for i in range(1, 2 * n + 1):
    print(b[i])
solve()
