def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ok = True
            for k in range(M):
                if S[i][k] == "x" and S[j][k] == "x":
                    ok = False
            if ok:
                ans += 1
    print(ans)
