def main():
    N,M = map(int,input().split())
    A = [input() for i in range(2*N)]
    rank = [[i+1,0] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            if A[rank[2*j][0]-1][i] == 'G':
                if A[rank[2*j+1][0]-1][i] == 'C':
                    rank[2*j][1] += 1
                elif A[rank[2*j+1][0]-1][i] == 'P':
                    rank[2*j+1][1] += 1
            elif A[rank[2*j][0]-1][i] == 'C':
                if A[rank[2*j+1][0]-1][i] == 'P':
                    rank[2*j][1] += 1
                elif A[rank[2*j+1][0]-1][i] == 'G':
                    rank[2*j+1][1] += 1
            elif A[rank[2*j][0]-1][i] == 'P':
                if A[rank[2*j+1][0]-1][i] == 'G':
                    rank[2*j][1] += 1
                elif A[rank[2*j+1][0]-1][i] == 'C':
                    rank[2*j+1][1] += 1
        rank.sort(key=lambda x: (-x[1],x[0]))
    for i in range(2*N):
        print(rank[i][0])

if __name__ == '__main__':
    main()