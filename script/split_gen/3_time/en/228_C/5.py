def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        if (P[i][0] + P[i][1] + P[i][2]) >= (K * 300):
            ans.append("Yes")
        else:
            ans.append("No")
    for i in range(N):
        print(ans[i])
