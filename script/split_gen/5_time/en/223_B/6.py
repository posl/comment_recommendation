def solve(S):
    # Complete this function
    l = len(S)
    min = S
    max = S
    for i in range(l):
        str = S[i:l] + S[0:i]
        if str < min:
            min = str
        if str > max:
            max = str
    return min, max
