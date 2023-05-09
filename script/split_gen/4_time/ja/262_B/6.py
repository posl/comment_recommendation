def solve():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        U, V = map(int, input().split())
        edges.append((U, V))
    # 頂点aから見たときに頂点b,cが存在するかどうかを判定
    # 頂点bから見たときに頂点a,cが存在するかどうかを判定
    # 頂点cから見たときに頂点a,bが存在するかどうかを判定
    # という風に、頂点a,b,cの順番を入れ替えて、全ての頂点について判定する
    # これで全ての頂点について判定できる
    ans = 0
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            for c in range(b+1, N+1):
                if (a, b) in edges and (b, c) in edges and (c, a) in edges:
                    ans += 1
    print(ans)
