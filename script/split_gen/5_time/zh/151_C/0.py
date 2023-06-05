def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        a,b = input().split()
        p.append(int(a))
        s.append(b)
    ac = 0
    wa = 0
    ac_list = []
    wa_list = []
    for i in range(m):
        if s[i] == 'AC':
            ac_list.append(p[i])
        else:
            wa_list.append(p[i])
    ac = len(set(ac_list))
    wa = len(set(wa_list))
    print(ac,wa)
