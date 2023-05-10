def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    rank = [(0, i) for i in range(2*N)]
    for i in range(M):
        rank.sort()
        new_rank = []
        for j in range(0, 2*N, 2):
            p1 = rank[j][1]
            p2 = rank[j+1][1]
            if A[p1][i] == A[p2][i]:
                new_rank.append(rank[j])
                new_rank.append(rank[j+1])
            elif A[p1][i] == 'G' and A[p2][i] == 'C':
                new_rank.append((rank[j][0]-1, rank[j][1]))
                new_rank.append((rank[j+1][0]+1, rank[j+1][1]))
            elif A[p1][i] == 'C' and A[p2][i] == 'P':
                new_rank.append((rank[j][0]-1, rank[j][1]))
                new_rank.append((rank[j+1][0]+1, rank[j+1][1]))
            elif A[p1][i] == 'P' and A[p2][i] == 'G':
                new_rank.append((rank[j][0]-1, rank[j][1]))
                new_rank.append((rank[j+1][0]+1, rank[j+1][1]))
            else:
                new_rank.append((rank[j][0]+1, rank[j][1]))
                new_rank.append((rank[j+1][0]-1, rank[j+1][1]))
        rank = new_rank
    rank.sort()
    for r in rank:
        print(r[1]+1)
