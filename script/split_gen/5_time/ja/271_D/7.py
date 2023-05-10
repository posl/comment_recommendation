def check(N,S,card):
    for i in range(N):
        card[i][0] = int(card[i][0])
        card[i][1] = int(card[i][1])
    for i in range(N):
        for j in range(N):
            if card[i][0] + card[j][1] == S:
                return True
    return False
