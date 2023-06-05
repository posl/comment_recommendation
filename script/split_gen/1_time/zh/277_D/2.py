def solve(n,m,ai):
    ai.sort()
    if n == 1:
        return 0
    if n == 2:
        if (ai[0] + 1) % m == ai[1]:
            return 0
        else:
            return ai[0] + 1
    if n == 3:
        if (ai[0] + 1) % m == ai[1] and (ai[1] + 1) % m == ai[2]:
            return 0
        elif (ai[0] + 1) % m == ai[1] and (ai[1] + 1) % m != ai[2]:
            return ai[2] + 1
        elif (ai[0] + 1) % m != ai[1] and (ai[1] + 1) % m == ai[2]:
            return ai[0] + 1
        else:
            return ai[0] + ai[1] + 2
    if n == 4:
        if (ai[0] + 1) % m == ai[1] and (ai[1] + 1) % m == ai[2] and (ai[2] + 1) % m == ai[3]:
            return 0
        elif (ai[0] + 1) % m == ai[1] and (ai[1] + 1) % m == ai[2] and (ai[2] + 1) % m != ai[3]:
            return ai[3] + 1
        elif (ai[0] + 1) % m == ai[1] and (ai[1] + 1) % m != ai[2] and (ai[2] + 1) % m == ai[3]:
            return ai[2] + 1
        elif (ai[0] + 1) % m != ai[1] and (ai[1] + 1) % m == ai[2] and (ai[2] + 1) % m == ai[3]:
            return ai[0] + 1
        elif (ai[0] + 1) % m == ai[1] and (ai[1] + 1) % m
