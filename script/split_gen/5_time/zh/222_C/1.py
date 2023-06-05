def main():
    N,M = map(int,input().split())
    A = [list(input()) for _ in range(2*N)]
    rank = [[i,0] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            p1 = rank[2*j][0]
            p2 = rank[2*j+1][0]
            if A[p1][i] == A[p2][i]:
                continue
            elif A[p1][i] == 'G':
                if A[p2][i] == 'C':
                    rank[2*j][1] -= 1
                else:
                    rank[2*j+1][1] -= 1
            elif A[p1][i] == 'C':
                if A[p2][i] == 'P':
                    rank[2*j][1] -= 1
                else:
                    rank[2*j+1][1] -= 1
            else:
                if A[p2][i] == 'G':
                    rank[2*j][1] -= 1
                else:
                    rank[2*j+1][1] -= 1
        rank.sort(key=lambda x:(x[1],x[0]))
    for i in range(2*N):
        print(rank[i][0]+1)
