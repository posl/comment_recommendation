def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                if s < p:
                    score += p
                else:
                    score += s
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                if p < r:
                    score += r
                else:
                    score += p
            else:
                score += r
        elif t[i] == 'p':
            if i >= k and t[i-k] == 'p':
                if s < r:
                    score += r
                else:
                    score += s
            else:
                score += s
    print(score)
