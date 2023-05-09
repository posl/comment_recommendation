def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if edges[i][0] == edges[j][0] or edges[i][0] == edges[j][1] or edges[i][1] == edges[j][0] or edges[i][1] == edges[j][1]:
                    continue
                if edges[j][0] == edges[k][0] or edges[j][0] == edges[k][1] or edges[j][1] == edges[k][0] or edges[j][1] == edges[k][1]:
                    continue
                if edges[i][0] == edges[k][0] or edges[i][0] == edges[k][1] or edges[i][1] == edges[k][0] or edges[i][1] == edges[k][1]:
                    continue
                ans += 1
    print(ans)
