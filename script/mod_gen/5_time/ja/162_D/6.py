def check(s, i, j, k):
  if (s[i] != s[j]) and (s[i] != s[k]) and (s[j] != s[k]):
    if (j - i) != (k - j):
      return True
  return False
n = int(input())
s = input()
r = s.count('R')
g = s.count('G')
b = s.count('B')
result = r * g * b
for i in range(n):
  for j in range(i+1, n):
    k = j + (j - i)
    if k < n:
      if check(s, i, j, k):
        result -= 1
print(result)

if __name__ == '__main__':
    check()