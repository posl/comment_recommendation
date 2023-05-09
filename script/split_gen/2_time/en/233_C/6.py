def main():
    N, X = map(int, input().split())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
        L[-1].pop(0)
    ans = 0
    for i in range(2**N):
        s = 1
        for j in range(N):
            if (i>>j)&1:
                s *= L[j][(i>>j)&1]
        if s == X:
            ans += 1
    print(ans)
