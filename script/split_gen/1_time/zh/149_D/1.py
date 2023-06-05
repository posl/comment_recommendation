def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                score += 0
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                score += 0
            else:
                score += r
        elif t[i] == 'p':
            if i >= k and t[i-k] == 'p':
                score += 0
            else:
                score += s
    print(score)
