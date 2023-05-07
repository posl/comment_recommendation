def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(2**N):
        p = 1
        for j in range(N):
            if (i>>j)&1:
                p *= L[j][(i>>j)&1]
        if p == X:
            ans += 1
    print(ans)
