def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    min_cnt = float('inf')
    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if (i>>j) & 1:
                score += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= p[rest_max]:
                continue
            cnt += need
        min_cnt = min(min_cnt, cnt)
    print(min_cnt)
