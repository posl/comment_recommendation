def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    C1 = [[0] * C for _ in range(3)]
    C2 = [[0] * C for _ in range(3)]
    C3 = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                C1[c[i][j] - 1][0] += 1
                C2[c[i][j] - 1][1] += 1
                C3[c[i][j] - 1][2] += 1
            elif (i + j) % 3 == 1:
                C1[c[i][j] - 1][1] += 1
                C2[c[i][j] - 1][2] += 1
                C3[c[i][j] - 1][0] += 1
            else:
                C1[c[i][j] - 1][2] += 1
                C2[c[i][j] - 1][0] += 1
                C3[c[i][j] - 1][1] += 1
    for i in range(C):
        for j in range(3):
            for k in range(C):
                D[j][i] += D[k][i] * C1[k][j]
    for i in range(C):
        for j in range(3):
            for k in range(C):
                D[j][i] += D[k][i] * C2[k][j]
    for i in range(C):
        for j in range(3):
            for k in range(C):
                D[j][i] += D[k][i] * C3[k][j]
    print(min(D[0]))
