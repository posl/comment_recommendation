def main():
  s = input()
  q = int(input())
  t = [0] * q
  f = [0] * q
  c = [''] * q
  for i in range(q):
    t[i], *f[i:], c[i] = input().split()
    f[i] = int(f[i])
  ans = ''
  rev = False
  for i in range(q):
    if t[i] == '1':
      rev = not rev
    else:
      if rev == (f[i] == 1):
        ans += c[i]
      else:
        ans = c[i] + ans
  if rev:
    ans = ans[::-1]
  print(ans)
