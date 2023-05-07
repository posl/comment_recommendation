def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = ""
    for i in range(N):
        ans += S[i]
        ans += "_"
    ans = ans[:-1]
    for i in range(M):
        if ans == T[i]:
            print(-1)
            return
    print(ans)
