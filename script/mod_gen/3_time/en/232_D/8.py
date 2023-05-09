def main():
  h, w = map(int, input().split())
  a = [input() for i in range(h)]
  visited = [[0]*w for i in range(h)]
  def dfs(i, j):
    if i < 0 or h <= i or j < 0 or w <= j or a[i][j] == "#":
      return
    if visited[i][j]:
      return
    visited[i][j] = 1
    dfs(i+1, j)
    dfs(i, j+1)
  dfs(0, 0)
  print(sum(sum(l) for l in visited))

if __name__ == '__main__':
    main()