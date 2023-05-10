def main():
  n, k = map(int, input().split())
  s = [input() for _ in range(n)]
  ans = 0
  for i in range(1, 2**n):
    t = []
    for j in range(n):
      if i & (1 << j):
        t.append(s[j])
    if len(t) < k: continue
    x = set()
    for j in range(len(t)):
      for c in t[j]:
        x.add(c)
    if len(x) == k:
      ans = max(ans, len(x))
  print(ans)

if __name__ == '__main__':
    main()