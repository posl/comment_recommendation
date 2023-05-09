def main():
    import sys
    from collections import deque
    M = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    p = tuple(map(int, input().split()))
    # 隣接リストを作る
    adj = [[] for _ in range(10)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    # 1から8の頂点について、p[i]からiへの移動を考える
    # 1から8の頂点について、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空き頂点として、BFSで移動させて、p[i]からiへの移動を考える
    # 9を空

if __name__ == '__main__':
    main()