def main():
    N, X, Y = map(int, input().split())
    #グラフの作成
    G = [[] for _ in range(N)]
    #頂点 i と 頂点 j の距離が 1 になるような整数の組 (i,j) (1 ≦ i < j ≦ N) は、
    #i+1, i+2, ..., N-1, N, 1, 2, 3, ..., i-1
    #i+1, i+2, ..., N-1, N, 1, 2, 3, ..., i-1
    for i in range(N):
        for j in range(i+1, N):
            if i+1 <= j+1 <= N:
                G[i].append(j)
                G[j].append(i)
            elif i+1 <= j+1-N <= N:
                G[i].append(j+1-N)
                G[j+1-N].append(i)
    #頂点 X と 頂点 Y の間に辺があります
    #X+1 < Y
    G[X-1].append(Y-1)
    G[Y-1].append(X-1)
    #print(G)
    #print()
    #k=1,2,...,N-1 について、以下の問題を解いてください。  
    #整数の組 (i,j) (1 ≦ i < j ≦ N) であって、 G において頂点 i と頂点 j の最短距離が k であるようなものの数を求めてください
    #print(N)
    for k in range(1, N):
        #print(k)
        #print()
        #print(N)
        #print()
        #print(G)
        #print()
        #print()
        #print()
        #print()
        #p
