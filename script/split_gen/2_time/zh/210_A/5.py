def main():
    N, Q = map(int, input().split())
    # print(N, Q)
    # print(type(N), type(Q))
    # print(type(N), type(Q))
    # print(type(N), type(Q))
    # a = [0] * (N - 1)
    # b = [0] * (N - 1)
    # c = [0] * Q
    # d = [0] * Q
    # for i in range(N - 1):
    #     a[i], b[i] = map(int, input().split())
    # for i in range(Q):
    #     c[i], d[i] = map(int, input().split())
    # print(a, b, c, d)
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    # print(graph)
    # print(graph[1][0])
    # print(graph[graph[1][0]][0])
    # print(graph[graph[graph[1][0]][0]][0])
    # print(graph[graph[graph[graph[1][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0]][0]][0]][0]][0])
    # print(graph[1][0])
    # print(graph[graph[1][0]][0])
    # print(graph[graph[graph[1][0]][0]][0])
    # print(graph[graph[graph[graph[1][0]][0]][
