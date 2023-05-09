def main():
    #input
    D, G = map(int, input().split())
    p = [0 for i in range(D)]
    c = [0 for i in range(D)]
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #calc
    ans = 10**10
    for i in range(2**D):
        cnt = 0
        score = 0
        for j in range(D):
            if (i >> j) & 1 == 1:
                cnt += p[j]
                score += (j+1)*100*p[j] + c[j]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for j in range(D-1, -1, -1):
                if (i >> j) & 1 == 0:
                    for k in range(p[j]):
                        if score >= G:
                            break
                        score += (j+1)*100
                        cnt += 1
                    if score >= G:
                        ans = min(ans, cnt)
                    break
    #output
    print(ans)

if __name__ == '__main__':
    main()