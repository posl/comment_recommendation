def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X = sorted(X)
    ans = 0
    if N >= M:
        print(ans)
        return
    else:
        ans = sum(X[-N:])-sum(X[:M-N])
        print(ans)
        return
