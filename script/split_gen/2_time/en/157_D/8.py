def main():
  N, M, K = map(int, input().split())
  f = [set() for _ in range(N)]
  b = [set() for _ in range(N)]
  for _ in range(M):
    a, b = map(int, input().split())
    f[a-1].add(b-1)
    f[b-1].add(a-1)
  for _ in range(K):
    c, d = map(int, input().split())
    b[c-1].add(d-1)
    b[d-1].add(c-1)
  ans = [0] * N
  for i in range(N):
    ans[i] = N - 1 - len(f[i]) - len(b[i])
  for i in range(N):
    for j in f[i]:
      if i in f[j]:
        ans[i] -= 1
        ans[j] -= 1
  print(*ans)
