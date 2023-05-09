def permute(s):
    if len(s) == 1:
        return [s]
    else:
        return [s[i] + p for i in range(len(s)) for p in permute(s[:i] + s[i+1:])]
