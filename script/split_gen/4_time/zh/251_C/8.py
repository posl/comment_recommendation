def best_score(n, s, t):
    max_score = {}
    for i in range(n):
        if s[i] not in max_score:
            max_score[s[i]] = t[i]
        else:
            if max_score[s[i]] < t[i]:
                max_score[s[i]] = t[i]
    max_score = sorted(max_score.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(max_score)):
        if max_score[i][1] == max_score[0][1]:
            return s.index(max_score[i][0]) + 1
