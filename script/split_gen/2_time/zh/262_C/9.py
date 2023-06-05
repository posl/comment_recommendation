def main():
    N, M = map(int, input().split())
    edge = []
    for i in range(M):
        edge.append(list(map(int, input().split())))
    edge.sort(key=lambda x: x[0])
    # print(edge)
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            if edge[i][0] == edge[j][0]:
                continue
            for k in range(j + 1, M):
                if edge[j][0] == edge[k][0]:
                    continue
                if edge[i][0] == edge[k][0]:
                    continue
                if edge[i][1] == edge[j][1] and edge[j][1] == edge[k][1]:
                    ans += 1
    print(ans)
