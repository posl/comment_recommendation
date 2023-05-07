def getPattern(H, W, A, B):
    #print("getPattern({},{},{},{})".format(H, W, A, B))
    if H == 0 and W == 0:
        return 1
    if H == 0:
        return getPattern(H, W-1, A, B) + getPattern(H, W-1, A-1, B)
    if W == 0:
        return getPattern(H-1, W, A, B) + getPattern(H-1, W, A, B-1)
    return getPattern(H, W-1, A, B) + getPattern(H-1, W, A, B)
