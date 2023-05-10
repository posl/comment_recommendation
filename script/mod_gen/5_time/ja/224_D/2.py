def main():
    M = int(input())
    u = []
    v = []
    for i in range(M):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
    p = list(map(int, input().split()))
    #print(M, u, v, p)
    # 隣接行列を作成
    adj = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(M):
        adj[u[i]-1][v[i]-1] = 1
        adj[v[i]-1][u[i]-1] = 1
    #print(adj)
    # 隣接行列を使って、頂点の隣接数を数える
    deg = [0 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            deg[i] += adj[i][j]
    #print(deg)
    # 頂点の隣接数が3の倍数でない場合は、操作できない
    for i in range(9):
        if deg[i] % 2 != 0:
            print(-1)
            exit()
    # 頂点の隣接数が6の倍数の場合は、操作回数は0
    if sum(deg) % 6 == 0:
        print(0)
        exit()
    # 頂点の隣接数が6の倍数ではない場合は、操作回数は1以上
    # 操作回数は最大で、隣接数が6の倍数の頂点を操作する回数
    # ただし、操作回数は2以上の偶数
    # また、操作回数が2以上の偶数の場合、隣接数が6の倍数の頂点を操作する回数は、
    # 2以上の偶数の場合は、隣接数が6の倍数の頂点を操作する回数は、
    # 1以上の奇数
    # 1以上の奇数
    # 1以上の奇数

if __name__ == '__main__':
    main()