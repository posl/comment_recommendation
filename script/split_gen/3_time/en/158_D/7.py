def reverse(s):
  return s[::-1]
s = input()
q = int(input())
t = [0] * q
f = [0] * q
c = [0] * q
for i in range(q):
  t[i] = input().split()
  if t[i][0] == '2':
    f[i] = int(t[i][1])
    c[i] = t[i][2]
for i in range(q):
  if t[i][0] == '1':
    s = reverse(s)
  else:
    if f[i] == 1:
      s = c[i] + s
    else:
      s = s + c[i]
print(s)
