def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        p[i],s[i] = input().split()
        p[i] = int(p[i])
    #print(p)
    #print(s)
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]-1] = 1
        elif s[i] == "WA" and ac[p[i]-1] == 0:
            wa[p[i]-1] += 1
    #print(ac)
    #print(wa)
    ac_count = 0
    wa_count = 0
    for i in range(n):
        if ac[i] == 1:
            ac_count += 1
            wa_count += wa[i]
    print(ac_count,wa_count)
