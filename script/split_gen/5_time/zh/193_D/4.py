def main():
    K = int(input())
    S = input()
    T = input()
    S = S[0:4] + S[5]
    T = T[0:4] + T[5]
    def score(s):
        score = 0
        for i in range(4):
            score += (i+1) * 10**s.count(str(i+1))
        return score
    def calc():
        s_score = score(S)
        t_score = score(T)
        if s_score > t_score:
            return 1
        elif s_score < t_score:
            return 0
        else:
            return 0.5
    # print(calc())
    # return
    def calc2():
        s_score = score(S)
        t_score = score(T)
        if S[4] == '#' and T[4] == '#':
            if s_score > t_score:
                return 1
            elif s_score < t_score:
                return 0
            else:
                return 0.5
        elif S[4] == '#' and T[4] != '#':
            if s_score > t_score:
                return 1
            elif s_score < t_score:
                return 0
            else:
                return 0.5
        elif S[4] != '#' and T[4] == '#':
            if s_score > t_score:
                return 1
            elif s_score < t_score:
                return 0
            else:
                return 0.5
        else:
            if s_score > t_score:
                return 1
            elif s_score < t_score:
                return 0
            else:
                return 0.5
    print(calc2())
    return
