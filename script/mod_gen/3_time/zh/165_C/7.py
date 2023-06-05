def max_score(n, m, q, score):
    max_score = 0
    for i in range(1, m+1):
        for j in range(1, m+1):
            for k in range(1, m+1):
                for l in range(1, m+1):
                    s = 0
                    for x in range(0, q):
                        if score[x][1] - score[x][0] == i:
                            s += score[x][2]
                        if score[x][1] - score[x][0] == j:
                            s += score[x][2]
                        if score[x][1] - score[x][0] == k:
                            s += score[x][2]
                        if score[x][1] - score[x][0] == l:
                            s += score[x][2]
                    if max_score < s:
                        max_score = s
    return max_score

if __name__ == '__main__':
    max_score()