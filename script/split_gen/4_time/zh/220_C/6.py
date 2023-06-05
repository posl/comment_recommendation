def solve(n, a, x):
  sum = 0
  i = 0
  while True:
    sum += a[i % n]
    i += 1
    if sum > x:
      return i
