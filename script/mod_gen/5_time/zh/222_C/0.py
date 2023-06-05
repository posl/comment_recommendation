def main():
    N,M = map(int,input().split())
    A = []
    for i in range(2*N):
        A.append(input())
    rank = [[i+1,0] for i in range(2*N)]
    for i in range(M):
        for j in range(0,2*N,2):
            if A[rank[j][0]-1][i] == A[rank[j+1][0]-1][i]:
                continue
            elif A[rank[j][0]-1][i] == 'G' and A[rank[j+1][0]-1][i] == 'C':
                rank[j][1] -= 1
            elif A[rank[j][0]-1][i] == 'C' and A[rank[j+1][0]-1][i] == 'P':
                rank[j][1] -= 1
            elif A[rank[j][0]-1][i] == 'P' and A[rank[j+1][0]-1][i] == 'G':
                rank[j][1] -= 1
            else:
                rank[j+1][1] -= 1
        rank.sort(key=lambda x:(x[1],x[0]))
    for i in range(2*N):
        print(rank[i][0])

if __name__ == '__main__':
    main()