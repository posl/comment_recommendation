def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9 + 7
    N,C = map(int,readline().split())
    D = [list(map(int,readline().split())) for _ in range(C)]
    c = [list(map(int,readline().split())) for _ in range(N)]
    ans = 10**18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(N):
                    for m in range(N):
                        if (l+m)%3 == 0:
                            tmp += D[c[l][m]-1][i]
                        elif (l+m)%3 == 1:
                            tmp += D[c[l][m]-1][j]
                        else:
                            tmp += D[c[l][m]-1][k]
                ans = min(ans,tmp)
    print(ans)
