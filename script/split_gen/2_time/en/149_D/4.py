def RPS_Battle(N,K,R,S,P,T):
    score=0
    for i in range(N):
        if i<K:
            if T[i]=='r':
                score+=P
            elif T[i]=='s':
                score+=R
            elif T[i]=='p':
                score+=S
        else:
            if T[i]=='r' and T[i-K]!='r':
                score+=P
            elif T[i]=='s' and T[i-K]!='s':
                score+=R
            elif T[i]=='p' and T[i-K]!='p':
                score+=S
    return score
