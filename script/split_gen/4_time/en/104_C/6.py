def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 1000000000
    for i in range(2**D):
        cnt = 0
        score = 0
        for j in range(D):
            if i >> j & 1:
                cnt += p[j]
                score += p[j]*(j+1)*100 + c[j]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for j in range(D-1, -1, -1):
                if not i >> j & 1:
                    for k in range(p[j]):
                        if score >= G:
                            break
                        score += (j+1)*100
                        cnt += 1
                    break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)
