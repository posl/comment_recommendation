def solve(N, M, k, s, p):
    ans = 0
    for i in range(1 << N):
        flag = True
        for j in range(M):
            cnt = 0
            for l in range(k[j]):
                if i & (1 << (s[j][l] - 1)):
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()