def main():
    N,M = map(int,input().split())
    A = []
    for i in range(2*N):
        A.append(input())
    rank = [[0,i] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            a = rank[2*j][1]
            b = rank[2*j+1][1]
            if A[a][i] == A[b][i]:
                continue
            elif A[a][i] == "G":
                if A[b][i] == "C":
                    rank[2*j][0] -= 1
                else:
                    rank[2*j+1][0] -= 1
            elif A[a][i] == "C":
                if A[b][i] == "P":
                    rank[2*j][0] -= 1
                else:
                    rank[2*j+1][0] -= 1
            else:
                if A[b][i] == "G":
                    rank[2*j][0] -= 1
                else:
                    rank[2*j+1][0] -= 1
        rank = sorted(rank)
    for i in range(2*N):
        print(rank[i][1]+1)
