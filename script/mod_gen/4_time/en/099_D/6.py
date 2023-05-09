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

if __name__ == '__main__':
    floyd_warshall()