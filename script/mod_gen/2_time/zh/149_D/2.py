def get_max_score(n, k, r, s, p, t):
    max_score = 0
    for i in range(n):
        if t[i] == 'r':
            max_score += p
        elif t[i] == 's':
            max_score += r
        else:
            max_score += s
    for i in range(n-k):
        if t[i] == 'r':
            if t[i+k] == 'r':
                max_score -= p
            elif t[i+k] == 's':
                max_score -= r
            else:
                max_score -= s
        elif t[i] == 's':
            if t[i+k] == 'r':
                max_score -= p
            elif t[i+k] == 's':
                max_score -= r
            else:
                max_score -= s
        else:
            if t[i+k] == 'r':
                max_score -= p
            elif t[i+k] == 's':
                max_score -= r
            else:
                max_score -= s
    return max_score
n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
print(get_max_score(n, k, r, s, p, t))
