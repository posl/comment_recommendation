def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    rank = []
    for i in range(2*N):
        rank.append((0, i+1))
    for i in range(M):
        for j in range(N):
            p1 = rank[2*j]
            p2 = rank[2*j+1]
            if A[p1[1]-1][i] == A[p2[1]-1][i]:
                continue
            elif A[p1[1]-1][i] == 'G' and A[p2[1]-1][i] == 'C':
                rank[2*j] = (p1[0]+1, p1[1])
            elif A[p1[1]-1][i] == 'C' and A[p2[1]-1][i] == 'P':
                rank[2*j] = (p1[0]+1, p1[1])
            elif A[p1[1]-1][i] == 'P' and A[p2[1]-1][i] == 'G':
                rank[2*j] = (p1[0]+1, p1[1])
            elif A[p1[1]-1][i] == 'G' and A[p2[1]-1][i] == 'P':
                rank[2*j+1] = (p2[0]+1, p2[1])
            elif A[p1[1]-1][i] == 'C' and A[p2[1]-1][i] == 'G':
                rank[2*j+1] = (p2[0]+1, p2[1])
            elif A[p1[1]-1][i] == 'P' and A[p2[1]-1][i] == 'C':
                rank[2*j+1] = (p2[0]+1, p2[1])
        rank.sort(key=lambda x: (-x[0], x[1]))
    for r in rank:
        print(r[1])

if __name__ == '__main__':
    main()