def main():
    N, M = map(int, input().split())
    #N, M = 5, 3
    #N, M = 5, 0
    #N, M = 4, 6
    if M == 0:
        print(N)
        return
    # 辺の情報を格納する
    edge = [[0 for i in range(2)] for j in range(M)]
    for i in range(M):
        edge[i] = list(map(int, input().split()))
    # 辺の情報を元に、頂点の情報を格納する
    vertex = [[0 for i in range(2)] for j in range(N)]
    for i in range(M):
        vertex[edge[i][0] - 1][0] += 1
        vertex[edge[i][0] - 1][1] = edge[i][0]
        vertex[edge[i][1] - 1][0] += 1
        vertex[edge[i][1] - 1][1] = edge[i][1]
    # 頂点の情報を元に、連結成分を求める
    connected_component = []
    for i in range(N):
        if vertex[i][0] == 0:
            connected_component.append([vertex[i][1]])
        else:
            for j in range(len(connected_component)):
                if vertex[i][1] in connected_component[j]:
                    connected_component[j].append(vertex[i][1])
                    break
            else:
                connected_component.append([vertex[i][1]])
    print(len(connected_component))
