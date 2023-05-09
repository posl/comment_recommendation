def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for s in S:
        if any(t in s for t in T):
            ans += 1
    print(ans)
