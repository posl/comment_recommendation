def janken(a,b):
    if a == b:
        return 0
    elif a == 'G':
        if b == 'C':
            return 1
        else:
            return -1
    elif a == 'C':
        if b == 'P':
            return 1
        else:
            return -1
    elif a == 'P':
        if b == 'G':
            return 1
        else:
            return -1
N, M = map(int, input().split())
A = [input() for _ in range(2*N)]
rank = [[i,0] for i in range(2*N)]
for i in range(M):
    for j in range(N):
        a = rank[2*j][0]
        b = rank[2*j+1][0]
        result = janken(A[a][i], A[b][i])
        if result == 1:
            rank[2*j][1] -= 1
        elif result == -1:
            rank[2*j+1][1] -= 1
    rank.sort(key=lambda x:(x[1], x[0]))
for i in range(2*N):
    print(rank[i][0]+1)

if __name__ == '__main__':
    janken()