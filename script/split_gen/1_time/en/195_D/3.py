def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        x = [0] * (M - (R - L + 1))
        cnt = 0
        for i in range(M):
            if i < L or i > R:
                x[cnt] = X[i]
                cnt += 1
        x.sort()
        v = [0] * N
        for i in range(N):
            for j in range(M - (R - L + 1)):
                if x[j] >= W[i]:
                    v[i] = V[i]
                    x[j] = 0
                    break
        print(sum(v))
