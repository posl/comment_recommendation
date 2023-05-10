def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        tmp = input().split()
        s.append(tmp[0])
        t.append(int(tmp[1]))
    #print(s)
    #print(t)
    maxt = max(t)
    #print(maxt)
    maxtindex = t.index(maxt)
    #print(maxtindex)
    maxs = s[maxtindex]
    #print(maxs)
    s.pop(maxtindex)
    t.pop(maxtindex)
    #print(s)
    #print(t)
    while maxs in s:
        maxsindex = s.index(maxs)
        s.pop(maxsindex)
        t.pop(maxsindex)
    #print(s)
    #print(t)
    print(t.index(max(t))+2)

if __name__ == '__main__':
    main()