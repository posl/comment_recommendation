def maxScore(N, K, R, S, P, T):
    # N: number of rounds
    # K: cannot use the hand used in the (i-K)-th round
    # R: Rock
    # S: Scissors
    # P: Paper
    # T: machine will play Rock, Paper, or Scissors in each round
    # return: maximum total score earned in the game
    score = 0
    prev = ""
    for i in range(N):
        if prev != T[i]:
            if T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            else:
                score += S
        else:
            if i >= K:
                if T[i-K] == "r":
                    if T[i] == "r":
                        score += P
                    elif T[i] == "s":
                        score += R
                    else:
                        score += S
                elif T[i-K] == "s":
                    if T[i] == "r":
                        score += P
                    elif T[i] == "s":
                        score += R
                    else:
                        score += S
                else:
                    if T[i] == "r":
                        score += P
                    elif T[i] == "s":
                        score += R
                    else:
                        score += S
        prev = T[i]
    return score
