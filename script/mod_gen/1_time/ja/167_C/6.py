def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**6
    for i in range(2**N):
        B = [0]*M
        C = 0
        for j in range(N):
            if (i>>j)&1:
                C += A[j][0]
                for k in range(M):
                    B[k] += A[j][k+1]
        if all(x>=X for x in B):
            ans = min(ans, C)
    if ans == 10**6:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()