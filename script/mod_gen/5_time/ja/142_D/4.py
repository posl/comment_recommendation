def gcd(a, b):
  if a < b:
    a, b = b, a
  if b == 0:
    return a
  return gcd(b, a % b)
A, B = map(int, input().split())
g = gcd(A, B)
