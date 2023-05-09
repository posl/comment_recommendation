def main():
    N, M = map(int, input().split())
    P_Y = []
    for i in range(M):
        P_Y.append(list(map(int, input().split())))
    P_Y.sort(key=lambda x: x[1])
    #print(P_Y)
    P = [0] * N
    for i in range(M):
        P[P_Y[i][0] - 1] += 1
    #print(P)
    P_Y2 = [0] * M
    for i in range(M):
        P_Y2[i] = [P_Y[i][0], P[P_Y[i][0] - 1]]
    #print(P_Y2)
    P_Y2.sort(key=lambda x: x[0])
    #print(P_Y2)
    P_Y3 = [0] * M
    for i in range(M):
        P_Y3[i] = [P_Y2[i][0], P_Y2[i][1], i + 1]
    #print(P_Y3)
    P_Y3.sort(key=lambda x: x[1])
    #print(P_Y3)
    for i in range(M):
        P_Y3[i] = [P_Y3[i][0], P_Y3[i][2]]
    #print(P_Y3)
    P_Y3.sort(key=lambda x: x[0])
    #print(P_Y3)
    for i in range(M):
        print(str(P_Y3[i][0]).zfill(6) + str(P_Y3[i][1]).zfill(6))
