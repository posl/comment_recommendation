def main():
    N, M = map(int, input().split())
    P_Y = [tuple(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])
    P = [0] * N
    P[P_Y[0][0] - 1] = 1
    c = 1
    for i in range(1, M):
        if P_Y[i - 1][0] != P_Y[i][0]:
            c = 1
        else:
            c += 1
        P[P_Y[i][0] - 1] = c
    for i in range(M):
        print(str(P_Y[i][0]).zfill(6) + str(P[i]).zfill(6))

if __name__ == '__main__':
    main()