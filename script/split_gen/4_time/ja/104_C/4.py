def main():
    d,g = map(int,input().split())
    p = []
    c = []
    for i in range(d):
        p_c = list(map(int,input().split()))
        p.append(p_c[0])
        c.append(p_c[1])
    min_count = 100000000
    for i in range(2**d):
        count = 0
        score = 0
        for j in range(d):
            if (i>>j) & 1 == 1:
                count += p[j]
                score += p[j]*(j+1)*100 + c[j]
        if score >= g:
            min_count = min(min_count,count)
        else:
            for j in range(d-1,-1,-1):
                if (i>>j) & 1 == 0:
                    for k in range(p[j]):
                        if score >= g:
                            break
                        else:
                            score += (j+1)*100
                            count += 1
            min_count = min(min_count,count)
    print(min_count)
