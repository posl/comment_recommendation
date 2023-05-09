def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    player = [i+1 for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            if A[player[2*j]-1][i] == A[player[2*j+1]-1][i]:
                continue
            elif A[player[2*j]-1][i] == 'G' and A[player[2*j+1]-1][i] == 'C':
                player[2*j], player[2*j+1] = player[2*j+1], player[2*j]
            elif A[player[2*j]-1][i] == 'C' and A[player[2*j+1]-1][i] == 'P':
                player[2*j], player[2*j+1] = player[2*j+1], player[2*j]
            elif A[player[2*j]-1][i] == 'P' and A[player[2*j+1]-1][i] == 'G':
                player[2*j], player[2*j+1] = player[2*j+1], player[2*j]
    for i in range(2*N):
        print(player[i])

if __name__ == '__main__':
    main()