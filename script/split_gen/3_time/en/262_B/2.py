def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                if edges[i][0] in edges[j] and edges[j][0] in edges[k] and edges[k][0] in edges[i]:
                    ans += 1
                elif edges[i][1] in edges[j] and edges[j][1] in edges[k] and edges[k][1] in edges[i]:
                    ans += 1
                elif edges[i][0] in edges[j] and edges[j][1] in edges[k] and edges[k][0] in edges[i]:
                    ans += 1
                elif edges[i][1] in edges[j] and edges[j][0] in edges[k] and edges[k][1] in edges[i]:
                    ans += 1
    print(ans)
