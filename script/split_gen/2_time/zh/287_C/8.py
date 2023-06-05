def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    ans = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                ans += 1
    print(ans)
