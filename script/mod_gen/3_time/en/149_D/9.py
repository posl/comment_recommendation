def RPS_Battle(N,K,R,S,P,T):
    #N: number of rounds
    #K: number of rounds that cannot be used the same hand
    #R: point for winning with Rock
    #S: point for winning with Scissors
    #P: point for winning with Paper
    #T: string of hands that the machine will play in each round
    #return: maximum total score earned in the game
    
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            else:
                score += S
        else:
            if T[i-K] == T[i]:
                T = T[:i] + 'x' + T[i+1:]
            else:
                if T[i] == 'r':
                    score += P
                elif T[i] == 's':
                    score += R
                else:
                    score += S
    return score

if __name__ == '__main__':
    RPS_Battle()