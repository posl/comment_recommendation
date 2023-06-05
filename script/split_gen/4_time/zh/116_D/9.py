def main():
    n,k = map(int,input().split())
    t_d = []
    for i in range(n):
        t_d.append(list(map(int,input().split())))
    t_d.sort(key=lambda x:x[1],reverse=True)
    t_d.sort(key=lambda x:x[0])
    t = []
    d = []
    for i in range(n):
        t.append(t_d[i][0])
        d.append(t_d[i][1])
    t_d = []
    for i in range(n):
        t_d.append([t[i],d[i]])
    t = []
    d = []
    for i in range(n):
        if t_d[i][0] not in t:
            t.append(t_d[i][0])
            d.append(t_d[i][1])
    #print(t)
    #print(d)
    t_d = []
    for i in range(len(t)):
        t_d.append([t[i],d[i]])
    #print(t_d)
    d = []
    for i in range(len(t_d)):
        d.append(t_d[i][1])
    #print(d)
    for i in range(len(d)-1):
        if d[i] < d[i+1]:
            d[i+1] = d[i]
    #print(d)
    d = d[::-1]
    #print(d)
    d = d[:k]
    #print(d)
    print(sum(d)+len(d)**2)
