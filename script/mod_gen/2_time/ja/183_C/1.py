def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j: continue
            for k in range(N):
                if k == i or k == j: continue
                for l in range(N):
                    if l == i or l == j or l == k: continue
                    for m in range(N):
                        if m == i or m == j or m == k or m == l: continue
                        if T[i][j] + T[j][k] + T[k][l] + T[l][m] + T[m][i] == K:
                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()