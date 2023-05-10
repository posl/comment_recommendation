def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort()
    ans = 0
    for i in range(m):
        for j in range(i+1, m):
            if edges[i][1] == edges[j][0]:
                for k in range(j+1, m):
                    if edges[i][0] == edges[k][0] and edges[j][1] == edges[k][1]:
                        ans += 1
    print(ans)
