def main():
    #入力
    M = int(input())
    edge = []
    for i in range(M):
        edge.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    #グラフの作成
    graph = [[0 for i in range(9)] for j in range(9)]
    for i in range(M):
        graph[edge[i][0] - 1][edge[i][1] - 1] = 1
        graph[edge[i][1] - 1][edge[i][0] - 1] = 1
    #状態の作成
    state = []
    for i in range(8):
        state.append(p[i] - 1)
    #状態のリストを作成
    state_list = [state]
    for i in range(8):
        for j in range(8):
            if i != j:
                state_list.append([state[i], state[j]])
    #状態のリストを作成
    for i in range(8):
        for j in range(8):
            for k in range(8):
                if i != j and j != k and k != i:
                    state_list.append([state[i], state[j], state[k]])
    for i in range(8):
        for j in range(8):
            for k in range(8):
                for l in range(8):
                    if i != j and j != k and k != l and l != i:
                        state_list.append([state[i], state[j], state[k], state[l]])
    for i in range(8):
        for j in range(8):
            for k in range(8):
                for l in range(8):
                    for m in range(8):
                        if i != j and j != k and k != l and l != m and m != i:
                            state_list.append([state[i], state[j], state[k], state[l], state[m]])
    for i in range(8):
        for j in range(8):
            for k in range(8):
                for l in range(8):
                    for m in range(8):
                        for n in range(8):
                            if i != j and j != k and k != l and l != m and m != n
