def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                t = t[:i] + ' ' + t[i+1:]
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                t = t[:i] + ' ' + t[i+1:]
            else:
                score += r
        else:
            if i >= k and t[i-k] == 'p':
                t = t[:i] + ' ' + t[i+1:]
            else:
                score += s
    print(score)

if __name__ == '__main__':
    main()