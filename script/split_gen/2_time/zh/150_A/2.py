def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    #print(n,k,r,s,p,t)
    #print(r,s,p)
    #print(t)
    score = 0
    for i in range(n):
        if t[i] == 'r':
            score += p
        elif t[i] == 's':
            score += r
        else:
            score += s
    for i in range(n-k):
        if t[i] == 'r' and t[i+k] == 'r':
            score -= p
        elif t[i] == 's' and t[i+k] == 's':
            score -= r
        elif t[i] == 'p' and t[i+k] == 'p':
            score -= s
    print(score)
