def check():
    N = input()
    S = [raw_input() for i in range(N)]
    if len(S) != len(set(S)):
        return False
    for s in S:
        if s[0] not in "HDCS":
            return False
        if s[1] not in "A23456789TJQK":
            return False
    return True
print "Yes" if check() else "No"
