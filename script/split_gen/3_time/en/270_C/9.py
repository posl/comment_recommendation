def main():
  # Input
  N,X,Y = map(int, input().split())
  # 全ての頂点についての隣接リスト
  adj = [[] for _ in range(N)]
  for _ in range(N-1):
    u,v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
  # BFS
  dist = [-1] * N
  dist[X-1] = 0
  q = [X-1]
  while q:
    v = q.pop()
    for w in adj[v]:
      if dist[w] == -1:
        dist[w] = dist[v] + 1
        q.append(w)
  # Output
  for i in range(N):
    if i != X-1:
      print(dist[i])
