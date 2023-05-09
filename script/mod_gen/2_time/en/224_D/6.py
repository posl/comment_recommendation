def solve():
    from collections import defaultdict
    from queue import Queue
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    pieces = list(map(int, input().split()))
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, 10):
        graph[i].append(i)
    # print(graph)
    # 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8
    # 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8
    # 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 0
    # 0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 0
    # 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 0, 9: 1
    # 0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 0, 8: 1
    # 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 0, 8: 1, 9: 2
    # 0: 3,

if __name__ == '__main__':
    solve()