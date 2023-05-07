def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = float("inf")
    for i in range(2**N):
        total = 0
        score = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                total += A[j][0]
                for k in range(M):
                    score[k] += A[j][k+1]
        if all(s >= X for s in score):
            ans = min(ans, total)
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()