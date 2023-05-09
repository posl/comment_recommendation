def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    P_Y = list(zip(P, Y))
    P_Y.sort(key=lambda x: x[1])
    P_Y.sort(key=lambda x: x[0])
    P_Y_dict = {}
    for i in range(M):
        if P_Y[i][0] in P_Y_dict:
            P_Y_dict[P_Y[i][0]] += 1
        else:
            P_Y_dict[P_Y[i][0]] = 1
        P_Y[i] = (str(P_Y[i][0]).zfill(6), str(P_Y_dict[P_Y[i][0]]).zfill(6))
    for i in range(M):
        print(P_Y[i][0] + P_Y[i][1])

if __name__ == '__main__':
    main()