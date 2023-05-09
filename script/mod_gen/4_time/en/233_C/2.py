def solve():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, 1 << N):
        cnt = 0
        num = 1
        for j in range(N):
            if i >> j & 1:
                cnt += 1
                num *= L[j][0]
        if cnt % 2 == 1:
            for j in range(num):
                tmp = 1
                for k in range(N):
                    if i >> k & 1:
                        tmp *= L[k][j % L[k][0] + 1]
                if tmp == X:
                    ans += 1
        else:
            for j in range(num):
                tmp = 1
                for k in range(N):
                    if i >> k & 1:
                        tmp *= L[k][j % L[k][0] + 1]
                if tmp == X:
                    ans -= 1
    print(ans)

if __name__ == '__main__':
    solve()