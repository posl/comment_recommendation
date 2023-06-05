def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: (x[0], x[1]))
    P = [0] * N
    Y = [0] * N
    for i in range(M):
        P[i] = P_Y[i][0]
        Y[i] = P_Y[i][1]
    cnt = [0] * N
    for i in range(M):
        cnt[P[i] - 1] += 1
    for i in range(M):
        print('{:06d}{:06d}'.format(P[i], cnt[P[i] - 1]))
        cnt[P[i] - 1] += 1
