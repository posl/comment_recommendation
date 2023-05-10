def replace_comma(S):
    S = list(S)
    K = S.count('"') // 2
    for i in range(1, K + 1):
        start = S.index('"')
        end = S.index('"', start + 1)
        for j in range(start, end + 1):
            if S[j] == ',':
                S[j] = '.'
    return "".join(S)
