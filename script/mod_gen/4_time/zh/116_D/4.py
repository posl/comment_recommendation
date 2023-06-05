def main():
    n,k = map(int,input().split())
    t_d = [list(map(int,input().split())) for _ in range(n)]
    t_d.sort(key=lambda x:x[1],reverse=True)
    #print(t_d)
    t = []
    d = []
    for i in range(n):
        t.append(t_d[i][0])
        d.append(t_d[i][1])
    #print(t,d)
    t_d = []
    for i in range(n):
        t_d.append([t[i],d[i]])
    #print(t_d)
    t_d.sort(key=lambda x:x[0])
    #print(t_d)
    t = []
    d = []
    for i in range(n):
        t.append(t_d[i][0])
        d.append(t_d[i][1])
    #print(t,d)
    t_d = []
    for i in range(n):
        t_d.append([t[i],d[i]])
    #print(t_d)
    s = 0
    t = []
    d = []
    for i in range(n):
        if t_d[i][0] not in t:
            t.append(t_d[i][0])
            d.append(t_d[i][1])
    #print(t,d)
    for i in range(k):
        s += d[i]
    #print(s)
    for i in range(n):
        if t_d[i][0] not in t[:k]:
            s += t_d[i][1]
    print(s)

if __name__ == '__main__':
    main()