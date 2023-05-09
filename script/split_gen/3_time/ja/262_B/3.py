def main():
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            for k in range(j + 1, M):
                if edge[i][0] == edge[j][0] and edge[j][0] == edge[k][0]:
                    continue
                elif edge[i][0] == edge[j][0] and edge[j][0] == edge[k][1]:
                    continue
                elif edge[i][0] == edge[j][1] and edge[j][1] == edge[k][0]:
                    continue
                elif edge[i][0] == edge[j][1] and edge[j][1] == edge[k][1]:
                    continue
                elif edge[i][1] == edge[j][0] and edge[j][0] == edge[k][0]:
                    continue
                elif edge[i][1] == edge[j][0] and edge[j][0] == edge[k][1]:
                    continue
                elif edge[i][1] == edge[j][1] and edge[j][1] == edge[k][0]:
                    continue
                elif edge[i][1] == edge[j][1] and edge[j][1] == edge[k][1]:
                    continue
                else:
                    ans += 1
    print(ans)
