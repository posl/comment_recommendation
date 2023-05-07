def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]
    A = [1]*N
    ans = 0
    def dfs(i):
        nonlocal ans
        if i == N:
            score = 0
            for j in range(Q):
                if A[ABCD[j][1]-1] - A[ABCD[j][0]-1] == ABCD[j][2]:
                    score += ABCD[j][3]
            ans = max(ans, score)
            return
        for j in range(A[i-1], M+1):
            A[i] = j
            dfs(i+1)
    dfs(1)
    print(ans)

if __name__ == '__main__':
    main()