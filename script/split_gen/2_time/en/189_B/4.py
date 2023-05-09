def main():
    N, X = map(int, input().split())
    V, P = [], []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    for i in range(N):
        X -= V[i]*P[i]/100
        if X < 0:
            print(i+1)
            return
    print(-1)
    return
