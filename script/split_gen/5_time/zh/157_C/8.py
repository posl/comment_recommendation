def find_min(N, M, s, c):
    #print(N)
    #print(M)
    #print(s)
    #print(c)
    #print("")
    #check if there is a number with N digits
    if N == 1:
        return c[0]
    if N == 2:
        if M == 1:
            if s[0] == 1:
                return c[0] * 10
            elif s[0] == 2:
                return c[0] + c[1] * 10
            else:
                return c[0]
        elif M == 2:
            if s[0] == 1:
                return c[0] * 10 + c[1]
            elif s[0] == 2:
                return c[1] * 10 + c[0]
            else:
                return c[0] * 10 + c[1]
        else:
            return -1
    if N == 3:
        if M == 1:
            if s[0] == 1:
                return c[0] * 100
            elif s[0] == 2:
                return c[0] * 10 + c[1] * 100
            elif s[0] == 3:
                return c[0] + c[1] * 10 + c[2] * 100
            else:
                return c[0]
        elif M == 2:
            if s[0] == 1:
                return c[0] * 100 + c[1]
            elif s[0] == 2:
                return c[1] * 100 + c[0] * 10
            elif s[0] == 3:
                return c[2] * 100 + c[0] + c[1] * 10
            else:
                return c[0] * 100 + c[1]
        elif M == 3:
            if s[0] == 1:
                return c[0] * 100 + c[1] * 10 + c[2]
            elif s[0] == 2:
                return c[1] * 100 + c[0] + c[2] * 10
            elif s[0] ==
