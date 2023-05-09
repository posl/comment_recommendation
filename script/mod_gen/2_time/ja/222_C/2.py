def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    rank = list(range(2*N))
    for j in range(M):
        next_rank = [-1] * (2*N)
        for i in range(N):
            a = rank[2*i]
            b = rank[2*i+1]
            if (A[a][j] == A[b][j]):
                next_rank[2*i] = a
                next_rank[2*i+1] = b
            elif (A[a][j] == 'G' and A[b][j] == 'C') or (A[a][j] == 'C' and A[b][j] == 'P') or (A[a][j] == 'P' and A[b][j] == 'G'):
                next_rank[2*i] = a
                next_rank[2*i+1] = b
            else:
                next_rank[2*i] = b
                next_rank[2*i+1] = a
        rank = next_rank
    for i in range(2*N):
        print(rank.index(i)+1)

if __name__ == '__main__':
    main()