Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 各色の数をカウント
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j] - 1] += 1

    # 各色の組み合わせについて、各色をどの色に塗り替えるかを全探索
    ans = 10 ** 18
    for c1 in range(C):
        for c2 in range(C):
            if c1 == c2:
                continue
            for c3 in range(C):
                if c1 == c3 or c2 == c3:
                    continue
                tmp = 0
                for i in range(C):
                    tmp += cnt[0][i] * D[i][c1]
                    tmp += cnt[1][i] * D[i][c2]
                    tmp += cnt[2][i] * D[i][c3]
                ans = min(ans, tmp)
    print(ans)

main()

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 剰余の和が0,1,2のときの色の個数を求める
    cnt = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i+j)%3][c[i][j]-1] += 1

    # 3色の組み合わせを全探索
    ans = 10**9
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue

                # 3色の組み合わせでの、色の個数の総和を求める
                tmp = 0
                for l in range(C):
                    tmp += cnt[0][l]*D[l][i]
                    tmp += cnt[1][l]*D[l][j]
                    tmp += cnt[2][l]*D[l][k]

                ans = min(ans, tmp)

    print(ans)

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * cnt[0][l]
                    tmp += D[l][j] * cnt[1][l]
                    tmp += D[l][k] * cnt[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    mod = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i+j)%3][c[i][j]-1] += 1
    ans = 10**10
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += mod[0][l]*D[l][i] + mod[1][l]*D[l][j] + mod[2][l]*D[l][k]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]
    d0 = [[0 for _ in range(c)] for _ in range(3)]
    for i in range(n):
        for j in range(n):
            d0[(i+j)%3][c[i][j]-1] += 1
    ans = 10**10
    for i in range(c):
        for j in range(c):
            for k in range(c):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(c):
                    tmp += d0[0][l] * d[l][i]
                    tmp += d0[1][l] * d[l][j]
                    tmp += d0[2][l] * d[l][k]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]

    ans = 10**9
    for i in range(c):
        for j in range(c):
            for k in range(c):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(n):
                    for m in range(n):
                        if (l+m)%3 == 0:
                            tmp += d[c[l][m]-1][i]
                        elif (l+m)%3 == 1:
                            tmp += d[c[l][m]-1][j]
                        else:
                            tmp += d[c[l][m]-1][k]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 7

def floyd_warshall(d):
    for k in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

d = floyd_warshall(D)

ans = 10**18
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if i == k or j == k:
                continue
            cnt = 0
            for l in range(N):
                for m in range(N):
                    if (l + m) % 3 == 0:
                        cnt += d[c[l][m]-1][i]
                    elif (l + m) % 3 == 1:
                        cnt += d[c[l][m]-1][j]
                    else:
                        cnt += d[c[l][m]-1][k]
            ans = min(ans, cnt)
print(ans)

=======
Suggestion 8

def main():
    n,c=map(int,input().strip().split())
    d=[list(map(int,input().strip().split())) for _ in range(c)]
    c=[list(map(int,input().strip().split())) for _ in range(n)]
    m=[0]*c
    for i in range(n):
        for j in range(n):
            m[(i+j)%3]+=d[c[i][j]-1]
    ans=10**9
    for i in range(c):
        for j in range(c):
            if i==j:continue
            for k in range(c):
                if i==k or j==k:continue
                ans=min(ans,m[i]+m[j]+m[k])
    print(ans)

=======
Suggestion 9

def main():
    N,C = map(int,input().split())
    D = [list(map(int,input().split())) for i in range(C)]
    c = [list(map(int,input().split())) for i in range(N)]
    mod = [0]*3
    for i in range(N):
        for j in range(N):
            mod[(i+j)%3] += D[c[i][j]-1][:]
    ans = 10**9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i==j or j==k or k==i:
                    continue
                ans = min(ans,mod[0][i]+mod[1][j]+mod[2][k])
    print(ans)

=======
Suggestion 10

def get_wrongness(c1, c2):
    return d[c1-1][c2-1]
