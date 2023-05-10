def main():
    N,M = map(int,input().split())
    A = [input() for _ in range(2*N)]
    rank = [[i+1,0] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            a = A[rank[2*j][0]-1][i]
            b = A[rank[2*j+1][0]-1][i]
            if a == 'G' and b == 'C':
                rank[2*j][1] += 1
            elif a == 'C' and b == 'P':
                rank[2*j][1] += 1
            elif a == 'P' and b == 'G':
                rank[2*j][1] += 1
            elif a == 'G' and b == 'P':
                rank[2*j+1][1] += 1
            elif a == 'C' and b == 'G':
                rank[2*j+1][1] += 1
            elif a == 'P' and b == 'C':
                rank[2*j+1][1] += 1
        rank.sort(key=lambda x:(-x[1],x[0]))
    for i in range(2*N):
        print(rank[i][0])

if __name__ == '__main__':
    main()