def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    #print(tree)
    #print(tree[0])
    #print(tree[1])
    #print(tree[2])
    #print(tree[3])
    #print(tree[4])
    
    #1からの距離を求める
    dist1 = [0] * N
    dist1[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in tree[v]:
            if dist1[u] == 0:
                dist1[u] = dist1[v] + w
                stack.append(u)
    #print(dist1)
    
    #Nからの距離を求める
    dist2 = [0] * N
    dist2[N - 1] = 0
    stack = [N - 1]
    while stack:
        v = stack.pop()
        for u, w in tree[v]:
            if dist2[u] == 0:
                dist2[u] = dist2[v] + w
                stack.append(u)
    #print(dist2)
    
    #1からの距離とNからの距離の差を求める
    dist3 = []
    for i in range(N):
        dist3.append(dist2[i] - dist1[i])
    #print(dist3)
    
    #1からの距離とNからの距離の差の絶対値の合計を求める
    dist4 = sum(list(map(abs, dist3)))
    #print(dist4)
    
    #1からの距離とNからの距離の差の絶対値の合計と1からの距離とNからの距離の差の絶対値の合計の差の合計を求める
    dist5 = sum(list(map(abs, dist3
