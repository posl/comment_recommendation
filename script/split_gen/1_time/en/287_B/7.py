def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = [0] * N
    for i in range(N):
        for j in range(M):
            if S[i][3:] == T[j]:
                ans[i] = 1
    print(sum(ans))
