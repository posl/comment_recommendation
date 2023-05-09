def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # print(c)
    # print(D)
    # print(N, C)
    # print(c)
    # print(D)
    # r = [[0]*C for _ in range(3)]
    # g = [[0]*C for _ in range(3)]
    # b = [[0]*C for _ in range(3)]
    # for i in range(N):
    #     for j in range(N):
    #         if (i+j) % 3 == 0:
    #             r[c[i][j]-1][0] += D[c[i][j]-1][0]
    #             r[c[i][j]-1][1] += D[c[i][j]-1][1]
    #             r[c[i][j]-1][2] += D[c[i][j]-1][2]
    #         elif (i+j) % 3 == 1:
    #             g[c[i][j]-1][0] += D[c[i][j]-1][0]
    #             g[c[i][j]-1][1] += D[c[i][j]-1][1]
    #             g[c[i][j]-1][2] += D[c[i][j]-1][2]
    #         elif (i+j) % 3 == 2:
    #             b[c[i][j]-1][0] += D[c[i][j]-1][0]
    #             b[c[i][j]-1][1] += D[c[i][j]-1][1]
    #             b[c[i][j]-1][2] += D[c[i][j]-1][2]
    # print(r)
    # print(g)
    # print(b)
    # r_min = 10000000000000000000
    # g_min = 10000000000000000000
    # b_min = 10000000000000000000
    # for i in range(C):
    #     for j in range(C):
    #         for k in range(C):
    #             if i != j and i != k and j != k:

if __name__ == '__main__':
    main()