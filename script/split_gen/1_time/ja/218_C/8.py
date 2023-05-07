def rotate(s):
    return ["".join([s[j][i] for j in range(len(s)-1, -1, -1)]) for i in range(len(s))]
