def main():
  n,m = map(int,input().split())
  g = [[] for i in range(n)]
  for i in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
  ans = 0
  for i in range(n):
    ans = max(ans, len(g[i])+1)
  print(ans)

if __name__ == '__main__':
    main()