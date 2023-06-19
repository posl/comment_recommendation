def main():
  N = int(input())
  #a,b = map(int,input().split())
  #A = list(map(int,input().split()))
  #S = input()
  #S = [input() for _ in range(H)]
  #S = [list(input()) for _ in range(H)]
  #S = [int(input()) for _ in range(N)]
  #S = [list(map(int,input().split())) for _ in range(N)]
  #S = [input().split() for _ in range(N)]
  #S = [list(map(int,input().split())) for _ in range(N)]
  #T = [int(input()) for _ in range(M)]
  #T = [list(map(int,input().split())) for _ in range(M)]
  #T = [input().split() for _ in range(M)]
  #T = [list(map(int,input().split())) for _ in range(M)]
  #G = [[] for _ in range(N)]
  G = [0]*(N+1)
  for _ in range(N-1):
    a,b = map(int,input().split())
    G[a] += 1
    G[b] += 1
  print(max(G))
  for i in range(1,N):
    print(i)
main()
