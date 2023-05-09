def rps_battle(N,K,R,S,P,T):
    #N = int(input())
    #K = int(input())
    #R = int(input())
    #S = int(input())
    #P = int(input())
    #T = input()
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            elif T[i] == 'p':
                score += S
        else:
            if T[i] == T[i-K]:
                T = T[:i]+'X'+T[i+1:]
            else:
                if T[i] == 'r':
                    score += P
                elif T[i] == 's':
                    score += R
                elif T[i] == 'p':
                    score += S
    return score
