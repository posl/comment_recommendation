def main():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for i in range(Q)]
    def dfs(A):
        if len(A) == N:
            score = 0
            for i in range(Q):
                if A[abcd[i][1]-1] - A[abcd[i][0]-1] == abcd[i][2]:
                    score += abcd[i][3]
            return score
        else:
            score = 0
            for i in range(A[-1], M+1):
                score = max(score, dfs(A+[i]))
            return score
    print(dfs([1]))

if __name__ == '__main__':
    main()