def move(s, k):
    #print(s, k)
    if k == 0:
        return s
    else:
        return move(s, k-1)[1:] + s[0]
