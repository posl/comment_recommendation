def main():
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                if edge[i][0] in edge[j] and edge[j][0] in edge[k] and edge[k][0] in edge[i]:
                    ans += 1
                elif edge[i][0] in edge[j] and edge[j][1] in edge[k] and edge[k][0] in edge[i]:
                    ans += 1
                elif edge[i][1] in edge[j] and edge[j][0] in edge[k] and edge[k][0] in edge[i]:
                    ans += 1
                elif edge[i][1] in edge[j] and edge[j][1] in edge[k] and edge[k][0] in edge[i]:
                    ans += 1
                elif edge[i][0] in edge[j] and edge[j][0] in edge[k] and edge[k][1] in edge[i]:
                    ans += 1
                elif edge[i][0] in edge[j] and edge[j][1] in edge[k] and edge[k][1] in edge[i]:
                    ans += 1
                elif edge[i][1] in edge[j] and edge[j][0] in edge[k] and edge[k][1] in edge[i]:
                    ans += 1
                elif edge[i][1] in edge[j] and edge[j][1] in edge[k] and edge[k][1] in edge[i]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()