def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    V_total = 0
    for i in range(N):
        V_total += V[i] * P[i]
        if V_total > X * 100:
            print(i + 1)
            break
    else:
        print(-1)
