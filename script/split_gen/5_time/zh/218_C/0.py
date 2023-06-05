def rotate90(S):
    S90 = []
    for i in range(len(S)):
        temp = ''
        for j in range(len(S)):
            temp += S[j][i]
        S90.append(temp[::-1])
    return S90
