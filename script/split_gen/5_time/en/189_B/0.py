def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    # print(N, X, V, P)
    sum = 0
    for i in range(N):
        sum += V[i] * P[i]
        if sum > X * 100:
            print(i+1)
            return
    print(-1)
