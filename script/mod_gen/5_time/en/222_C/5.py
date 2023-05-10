def rock_scissors_paper():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    players = [[i+1, 0] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            p1 = players[2*j]
            p2 = players[2*j+1]
            h1 = A[p1[0]-1][i]
            h2 = A[p2[0]-1][i]
            if h1 == 'G' and h2 == 'C':
                p1[1] += 1
            elif h1 == 'C' and h2 == 'P':
                p1[1] += 1
            elif h1 == 'P' and h2 == 'G':
                p1[1] += 1
            elif h1 == h2:
                continue
            else:
                p2[1] += 1
        players.sort(key=lambda x: (-x[1], x[0]))
    for i in range(2*N):
        print(players[i][0])
rock_scissors_paper()

if __name__ == '__main__':
    rock_scissors_paper()