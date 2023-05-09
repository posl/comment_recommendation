def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                if edges[i][0] == edges[j][0] and edges[j][0] == edges[k][0]:
                    continue
                if edges[i][0] == edges[j][0] and edges[j][0] == edges[k][1]:
                    continue
                if edges[i][0] == edges[j][1] and edges[j][1] == edges[k][0]:
                    continue
                if edges[i][0] == edges[j][1] and edges[j][1] == edges[k][1]:
                    continue
                if edges[i][1] == edges[j][0] and edges[j][0] == edges[k][0]:
                    continue
                if edges[i][1] == edges[j][0] and edges[j][0] == edges[k][1]:
                    continue
                if edges[i][1] == edges[j][1] and edges[j][1] == edges[k][0]:
                    continue
                if edges[i][1] == edges[j][1] and edges[j][1] == edges[k][1]:
                    continue
                if edges[i][0] == edges[j][0] or edges[i][0] == edges[j][1] or edges[i][0] == edges[k][0] or edges[i][0] == edges[k][1]:
                    continue
                if edges[i][1] == edges[j][0] or edges[i][1] == edges[j][1] or edges[i][1] == edges[k][0] or edges[i][1] == edges[k][1]:
                    continue
                if edges[j][0] == edges[k][0] or edges[j][0] == edges[k][1]:
                    continue
                if edges[j][1] == edges[k][0] or edges[j][1] == edges[k][1]:
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()