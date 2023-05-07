def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    ans = -1
    for i in range(N):
        if V[i] * P[i] / 100 > X:
            ans = i + 1
            break
        else:
            X -= V[i] * P[i] / 100
    print(ans)
