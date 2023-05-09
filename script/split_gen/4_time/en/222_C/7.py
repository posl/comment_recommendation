def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(N, M)
    #print(A)
    rank = [[i+1, 0] for i in range(2*N)]
    #print(rank)
    for i in range(M):
        for j in range(N):
            #print(i, j)
            p1 = rank[2*j][0] - 1
            p2 = rank[2*j+1][0] - 1
            #print(p1, p2)
            h1 = A[p1][i]
            h2 = A[p2][i]
            #print(h1, h2)
            if (h1 == 'G' and h2 == 'C') or (h1 == 'C' and h2 == 'P') or (h1 == 'P' and h2 == 'G'):
                rank[2*j][1] -= 1
                rank[2*j+1][1] += 1
            elif (h1 == 'G' and h2 == 'P') or (h1 == 'C' and h2 == 'G') or (h1 == 'P' and h2 == 'C'):
                rank[2*j][1] += 1
                rank[2*j+1][1] -= 1
            else:
                pass
        rank.sort(key=lambda x: x[1])
        rank.sort(key=lambda x: x[0])
        #print(rank)
    for i in range(2*N):
        print(rank[i][0])
    return
