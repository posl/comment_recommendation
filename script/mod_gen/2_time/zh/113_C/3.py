def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])
    P_Y_dict = {}
    for i in range(M):
        P_Y_dict[P_Y[i][0]] = P_Y_dict.get(P_Y[i][0], []) + [i]
    ans = [0] * M
    for i in range(1, N + 1):
        for j in range(len(P_Y_dict[i])):
            ans[P_Y_dict[i][j]] = str(i).zfill(6) + str(j + 1).zfill(6)
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()