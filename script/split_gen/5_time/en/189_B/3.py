def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    x = 0
    for i in range(N):
        x += V[i] * (P[i] / 100)
        if x > X:
            print(i+1)
            return
    print(-1)
main()
