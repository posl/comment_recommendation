def dfs(i, n, m, a, b, c, d, visited):
  if i == n:
    return True
  for j in range(n):
    if visited[j]:
      continue
    if a[i] == c[j] and b[i] == d[j]:
      visited[j] = True
      if dfs(i + 1, n, m, a, b, c, d, visited):
        return True
      visited[j] = False
  return False

if __name__ == '__main__':
    dfs()