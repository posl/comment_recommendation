def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if S[i].count("o") + S[j].count("o") >= M:
                ans += 1
    print(ans)
