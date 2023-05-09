def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    P = [p - 1 for p in P]
    P_index = [0] * N
    P_list = [[] for _ in range(N)]
    for i, p in enumerate(P):
        P_list[p].append((Y[i], i))
    for i in range(N):
        P_list[i].sort()
    for i in range(N):
        for j in range(len(P_list[i])):
            P_list[i][j] = (P_list[i][j][0], i, j + 1)
    P_list.sort(key=lambda x: x[0][1])
    P_list.sort(key=lambda x: x[0][0])
    ans = [0] * M
    for i in range(N):
        for j in range(len(P_list[i])):
            ans[P_list[i][j][1]] = str(P_list[i][j][1] + 1).zfill(6) + str(P_list[i][j][2]).zfill(6)
    print('
'.join(ans))

if __name__ == '__main__':
    main()