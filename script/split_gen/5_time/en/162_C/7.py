def gcd(x, y):
  if x < y:
    x, y = y, x
  if y == 0:
    return x
  return gcd(y, x % y)
K = int(input())
ans = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    for c in range(1, K+1):
      ans += gcd(gcd(a, b), c)
print(ans)
