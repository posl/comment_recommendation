def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for s in S:
        ans += T.count(s[-3:])
    print(ans)
