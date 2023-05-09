def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    #print(P)
    #print(Y)
    # sort
    sorted_Y = sorted(Y)
    #print(sorted_Y)
    # sort by prefecture
    sorted_P = sorted(P)
    #print(sorted_P)
    # sorted index
    sorted_Y_index = sorted(range(len(Y)), key=lambda k: Y[k])
    #print(sorted_Y_index)
    # sorted Y by prefecture
    sorted_Y_by_P = []
    for i in range(N):
        sorted_Y_by_P.append([])
    for i in range(M):
        sorted_Y_by_P[P[sorted_Y_index[i]]-1].append(sorted_Y_index[i])
    #print(sorted_Y_by_P)
    for i in range(N):
        for j in range(len(sorted_Y_by_P[i])):
            sorted_Y_by_P[i][j] = str(sorted_Y_by_P[i][j]+1).zfill(6)
    #print(sorted_Y_by_P)
    # print answer
    for i in range(M):
        print(str(P[i]).zfill(6)+sorted_Y_by_P[P[i]-1].pop(0))
