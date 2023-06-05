def main():
    a,b,q = map(int,input().split())
    s = []
    t = []
    x = []
    for _ in range(a):
        s.append(int(input()))
    for _ in range(b):
        t.append(int(input()))
    for _ in range(q):
        x.append(int(input()))
    for i in range(q):
        s.append(x[i])
        t.append(x[i])
        s.sort()
        t.sort()
        index_s = s.index(x[i])
        index_t = t.index(x[i])
        if index_s == 0:
            print(abs(t[0]-x[i]))
        elif index_s == len(s)-1:
            print(abs(s[-1]-x[i]))
        else:
            if index_s <= index_t:
                print(min(abs(t[index_t]-x[i]),abs(s[index_s-1]-x[i])+abs(s[index_s-1]-t[index_t]),abs(s[index_s]-x[i])+abs(s[index_s]-t[index_t])))
            else:
                print(min(abs(s[index_s]-x[i]),abs(t[index_t-1]-x[i])+abs(t[index_t-1]-s[index_s]),abs(t[index_t]-x[i])+abs(t[index_t]-s[index_s])))

if __name__ == '__main__':
    main()