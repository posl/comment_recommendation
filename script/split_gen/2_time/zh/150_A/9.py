def get_max_score(n, k, r, s, p, t):
    #print(n, k, r, s, p, t)
    sum = 0
    for i in range(n):
        if t[i] == 'r':
            sum += p
        elif t[i] == 's':
            sum += r
        elif t[i] == 'p':
            sum += s
    #print("sum=", sum)
    for i in range(k):
        if t[i] == t[i+k]:
            if i+k+k < n:
                if t[i+k+k] == 'r':
                    sum -= p
                elif t[i+k+k] == 's':
                    sum -= r
                elif t[i+k+k] == 'p':
                    sum -= s
            else:
                sum -= 0
    return sum
