def main():
    M = int(input())
    graph = [[0] * 9 for i in range(9)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = 1
        graph[v - 1][u - 1] = 1
    pieces = list(map(int, input().split()))
    pieces = [p - 1 for p in pieces]
    pieces = [pieces.inde
