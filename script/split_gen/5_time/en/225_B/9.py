def check_star(n, edges):
  #print(n, edges)
  if len(edges) != n-1:
    return False
  for i in range(n-1):
    if edges[i][0] > edges[i][1]:
      edges[i][0], edges[i][1] = edges[i][1], edges[i][0]
  edges.sort()
  #print(edges)
  for i in range(n-2):
    if edges[i][0] == edges[i+1][0] and edges[i][1] == edges[i+1][1]:
      return False
  for i in range(n-1):
    if edges[i][0] != i+1:
      return False
  return True
n = int(input())
edges = []
for i in range(n-1):
  a, b = map(int, input().split())
  edges.append([a, b])
