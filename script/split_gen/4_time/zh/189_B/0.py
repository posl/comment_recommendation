def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    total = 0
    for i in range(N):
        total += V[i] * P[i]
        if total > X * 100:
            print(i + 1)
            return
    print(-1)
    return
main()
