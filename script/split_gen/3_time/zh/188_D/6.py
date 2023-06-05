def main():
    n,c = map(int,input().split())
    s = []
    e = []
    p = []
    for i in range(n):
        a,b,d = map(int,input().split())
        s.append(a)
        e.append(b)
        p.append(d)
    s_e = list(zip(s,e,p))
    s_e.sort()
    s_e.append([c+1,c+1,0])
    #print(s_e)
    #print(s)
    #print(e)
    #print(p)
    p_sum = 0
    p_max = 0
    for i in range(n):
        if s_e[i][1] == s_e[i+1][0]:
            p_sum += s_e[i][2]
            if p_max < p_sum:
                p_max = p_sum
        else:
            p_sum += s_e[i][2]
            if p_max < p_sum:
                p_max = p_sum
            p_sum = 0
    print(p_max)
