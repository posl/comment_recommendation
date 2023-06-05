def main():
    N, M = map(int, input().split())
    p = []
    s = []
    for i in range(M):
        pi, si = input().split()
        p.append(int(pi))
        s.append(si)
    #print(p)
    #print(s)
    ac = 0
    wa = 0
    ac_list = [0]*N
    wa_list = [0]*N
    for i in range(M):
        if s[i] == 'AC':
            if ac_list[p[i]-1] == 0:
                ac_list[p[i]-1] = 1
                ac += 1
                wa += wa_list[p[i]-1]
        else:
            if ac_list[p[i]-1] == 0:
                wa_list[p[i]-1] += 1
    print(ac, wa)
