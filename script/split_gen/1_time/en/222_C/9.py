def solve(N, M, A):
    # 1. Create a list of players with their ID and number of wins
    players = []
    for i in range(2*N):
        players.append([i+1, 0]) # ID, number of wins
    # 2. Play matches
    for i in range(M):
        # 2.1. Create a list of matches
        matches = []
        for k in range(N):
            matches.append([players[2*k], players[2*k+1]])
        # 2.2. Play matches
        for match in matches:
            if A[match[0][0]-1][i] == 'G' and A[match[1][0]-1][i] == 'C':
                match[0][1] += 1
            elif A[match[0][0]-1][i] == 'C' and A[match[1][0]-1][i] == 'P':
                match[0][1] += 1
            elif A[match[0][0]-1][i] == 'P' and A[match[1][0]-1][i] == 'G':
                match[0][1] += 1
            elif A[match[1][0]-1][i] == 'G' and A[match[0][0]-1][i] == 'C':
                match[1][1] += 1
            elif A[match[1][0]-1][i] == 'C' and A[match[0][0]-1][i] == 'P':
                match[1][1] += 1
            elif A[match[1][0]-1][i] == 'P' and A[match[0][0]-1][i] == 'G':
                match[1][1] += 1
        # 2.3. Sort by number of wins and ID
        players = sorted(matches, key=lambda x: (-x[0][1], x[0][0])) + sorted(matches, key=lambda x: (-x[1][1], x[1][0]))
    # 3. Print solution
    for player in players:
        print(player[0][0])
