def calc_score(n,x,s):
    score = x
    for i in range(n):
        if s[i] == 'o':
            score += 1
        elif s[i] == 'x' and score > 0:
            score -= 1
    return score
n,x = map(int, input().split())
s = input()
print(calc_score(n,x,s))
