def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        x,y = input().split()
        p.append(int(x))
        s.append(y)
    p = [x-1 for x in p]
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]] = 1
        else:
            if ac[p[i]] == 0:
                wa[p[i]] += 1
    print(sum(ac),sum([ac[i]*wa[i] for i in range(n)]))
