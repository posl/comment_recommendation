def main():
    N, M = map(int, input().split())
    D = {}
    for i in range(1, N + 1):
        D[i] = []
    for i in range(M):
        P, Y = map(int, input().split())
        D[P].append([Y, i])
    for i in range(1, N + 1):
        D[i].sort()
        for j in range(len(D[i])):
            D[i][j][0] = str(D[i][j][0]).zfill(6)
            D[i][j][1] = str(D[i][j][1] + 1).zfill(6)
    ans = []
    for i in range(1, N + 1):
        for j in range(len(D[i])):
            ans.append(str(i).zfill(6) + str(D[i][j][1]))
    for i in ans:
        print(i)
