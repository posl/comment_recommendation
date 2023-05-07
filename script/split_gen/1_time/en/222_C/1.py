def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    player = [i+1 for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            if A[player[2*j]-1][i] == 'G':
                if A[player[2*j+1]-1][i] == 'C':
                    player[2*j], player[2*j+1] = player[2*j+1], player[2*j]
            elif A[player[2*j]-1][i] == 'C':
                if A[player[2*j+1]-1][i] == 'P':
                    player[2*j], player[2*j+1] = player[2*j+1], player[2*j]
            elif A[player[2*j]-1][i] == 'P':
                if A[player[2*j+1]-1][i] == 'G':
                    player[2*j], player[2*j+1] = player[2*j+1], player[2*j]
    for i in range(2*N):
        print(player[i])
