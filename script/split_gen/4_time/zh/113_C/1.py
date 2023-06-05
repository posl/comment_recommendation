def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])
    P_Y_dict = {}
    for i in range(M):
        P_Y_dict[P_Y[i][0]] = P_Y_dict.get(P_Y[i][0], 0) + 1
    for i in range(M):
        print(str(P_Y[i][0]).zfill(6) + str(P_Y_dict[P_Y[i][0]]).zfill(6))
