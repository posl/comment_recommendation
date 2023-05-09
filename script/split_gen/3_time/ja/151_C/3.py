def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        p_i,s_i = input().split()
        p.append(int(p_i))
        s.append(s_i)
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]-1] = 1
        elif s[i] == "WA" and ac[p[i]-1] == 0:
            wa[p[i]-1] += 1
    print(sum(ac),sum(wa))
