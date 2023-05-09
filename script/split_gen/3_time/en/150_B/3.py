def countABC(S):
    count = 0
    for i in range(len(S) - 2):
        if S[i:i+3] == 'ABC':
            count += 1
    return count
