def problems251_c():
    n = int(input())
    score = {}
    for i in range(n):
        s, t = input().split()
        if s not in score:
            score[s] = int(t)
        else:
            score[s] = max(score[s], int(t))
    max_score = max(score.values())
    for i in range(n):
        if score[s] == max_score:
            print(i + 1)
            break
