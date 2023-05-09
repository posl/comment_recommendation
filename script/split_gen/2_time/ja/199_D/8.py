def main():
    import sys
    input = sys.stdin.readline
    
    n,m = map(int,input().split())
    if m == 0:
        print(3**n)
        return
    
    #辺のリストを作成
    edge = [list(map(int,input().split())) for _ in range(m)]
    
    #各頂点の隣接リストを作成
    adj = [[] for _ in range(n)]
    for a,b in edge:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    
    #頂点を赤、緑、青のいずれかで塗る
    #辺で直接結ばれている 2 頂点は必ず異なる色で塗られている
    #なお、使われない色があっても構いません。
    ans = 0
    #頂点iを赤で塗る場合
    for i in range(n):
        #頂点iに隣接している頂点を赤で塗ることはできない
        for j in adj[i]:
            if j < i:
                break
        else:
            #頂点iに隣接している頂点を緑で塗る場合
            for k in range(n):
                #頂点kに隣接している頂点を緑で塗ることはできない
                for l in adj[k]:
                    if l < k:
                        break
                else:
                    #頂点iと頂点kに隣接している頂点を青で塗る場合
                    for m in range(n):
                        #頂点mに隣接している頂点を青で塗ることはできない
                        for n in adj[m]:
                            if n < m:
                                break
                        else:
                            #頂点iと頂点kに隣接している頂点を青で塗ることはできる
