def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    ans = 0
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if edges[i][1] in edges[j] and edges[i][0] in edges[j]:
                ans += 1
    print(ans)
