def check(s, N, M, AB, K, CD):
    ans = 0
    for i in range(M):
        if s[AB[i][0]-1] and s[AB[i][1]-1]:
            ans += 1
    return ans
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]
ans = 0
for i in range(2**K):
    s = [0]*N
    for j in range(K):
        if (i>>j)&1:
            s[CD[j][0]-1] = 1
        else:
            s[CD[j][1]-1] = 1
    ans = max(ans, check(s, N, M, AB, K, CD))
print(ans)

if __name__ == '__main__':
    check()