def main():
    d,g = map(int,input().split())
    p = []
    c = []
    for i in range(d):
        a,b = map(int,input().split())
        p.append(a)
        c.append(b)
    ans = []
    for i in range(1<<d):
        score = 0
        count = 0
        for j in range(d):
            if i&(1<<j):
                score += p[j]*(j+1)*100 + c[j]
                count += p[j]
        if score >= g:
            ans.append(count)
        else:
            for j in range(d-1,-1,-1):
                if i&(1<<j):
                    continue
                for k in range(p[j]):
                    if score >= g:
                        break
                    score += (j+1)*100
                    count += 1
            ans.append(count)
    print(min(ans))

if __name__ == '__main__':
    main()