def main():
    N, K = map(int, input().split())
    T = []
    D = []
    for i in range(N):
        t, d = map(int, input().split())
        T.append(t)
        D.append(d)
    T = list(set(T))
    T = sorted(T, key=lambda x: T.index(x))
    T = [0] + T
    D = sorted(D, reverse=True)
    D = [0] + D
    ans = 0
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            if T.index(T[j]) < i:
                continue
            ans = max(ans, sum(D[1:i]) + i * i + sum(D[i + 1:j]))
            break
    print(ans)
