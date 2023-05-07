def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += S[i][2]
        for j in range(i+1, N):
            if S[i][0] == S[j][0] and S[i][1] == S[j][1]:
                ans -= S[j][2]
                break
    print(ans)
