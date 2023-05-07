def prefix(S, T):
    if S == T[:len(S)]:
        return "Yes"
    return "No"
