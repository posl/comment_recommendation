def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    X = X * 1000
    alcohol = 0
    for i in range(N):
        alcohol += V[i] * P[i]
        if alcohol > X:
            print(i + 1)
            exit()
    print(-1)
