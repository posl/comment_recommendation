def minmax(S):
    min_str = S
    max_str = S
    for i in range(1, len(S)):
        S = S[1:] + S[0]
        if S < min_str:
            min_str = S
        if S > max_str:
            max_str = S
    return min_str, max_str
