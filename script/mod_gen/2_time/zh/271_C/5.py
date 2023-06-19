def solve(n, a):
  result = 0
  for i in range(n):
    if a[i] <= result + 1:
      result += a[i]
    else:
      break
  return result + 1

if __name__ == '__main__':
    solve()