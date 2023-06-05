def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_tmp, s_tmp = input().split()
        p.append(int(p_tmp))
        s.append(s_tmp)
    #print(p)
    #print(s)
    ac = 0
    wa = 0
    for i in range(n):
        if i+1 in p:
            index = p.index(i+1)
            if s[index] == 'AC':
                ac += 1
            else:
                wa += 1
    print(ac, wa)
