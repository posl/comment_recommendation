def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    alcohol = 0
    for i in range(N):
        alcohol += (V[i] * P[i])
        if alcohol > X * 100:
            print(i+1)
            return
    print(-1)
    return
