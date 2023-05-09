def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    cnt += 1
            if cnt == M:
                ans += 1
    print(ans)
