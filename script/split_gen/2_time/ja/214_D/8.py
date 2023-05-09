def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    edges.sort(key=lambda x: x[2])
    # 頂点iからの距離の累積和
    # 重みの和
    dist = [0] * (N + 1)
    for u, v, w in edges:
        dist[u] += w
        dist[v] += w
    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w
    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w
    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w
    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w
    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w
