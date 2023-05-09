def main():
    import sys
    from math import gcd
    input = sys.stdin.readline
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    A = [L[i][1:] for i in range(N)]
    G = [gcd(A[i][j], A[i][j+1]) for i in range(N) for j in range(L[i][0]-1)]
    for i in range(N):
        for j in range(L[i][0]):
            G.append(gcd(X, A[i][j]))
    G = list(set(G))
    ans = 0
    for i in range(len(G)):
        cnt = 0
        for j in range(N):
            for k in range(L[j][0]):
                if A[j][k] % G[i] == 0:
                    cnt += 1
        if cnt == N * L[0][0]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()