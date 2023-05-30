def exam(n, k, p):
  ans = 0
  for i in range(n):
    if sum(p[i]) >= 350:
      ans += 1
  return 'Yes' if ans >= k else 'No'
n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
print(exam(n, k, p))
