def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if i >= k and t[i] == t[i-k] and t[i] == 'r':
            t = t[:i] + 'p' + t[i+1:]
        elif i >= k and t[i] == t[i-k] and t[i] == 's':
            t = t[:i] + 'r' + t[i+1:]
        elif i >= k and t[i] == t[i-k] and t[i] == 'p':
            t = t[:i] + 's' + t[i+1:]
        if t[i] == 'r':
            score += p
        elif t[i] == 's':
            score += r
        elif t[i] == 'p':
            score += s
    print(score)

if __name__ == '__main__':
    main()