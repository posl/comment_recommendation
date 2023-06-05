def main():
    n,k = map(int,input().split())
    t = []
    d = []
    for i in range(n):
        a,b = map(int,input().split())
        t.append(a)
        d.append(b)
    #print(t)
    #print(d)
    d2 = []
    for i in range(n):
        d2.append([d[i],t[i]])
    #print(d2)
    d2.sort(reverse=True)
    #print(d2)
    d3 = []
    d4 = []
    for i in range(k):
        d3.append(d2[i][0])
        d4.append(d2[i][1])
    #print(d3)
    #print(d4)
    d4 = list(set(d4))
    #print(d4)
    d5 = []
    for i in range(len(d4)):
        d5.append(d4[i]*d4[i])
    #print(d5)
    d6 = []
    for i in range(len(d4)):
        d6.append(0)
    #print(d6)
    for i in range(len(d4)):
        for j in range(len(d)):
            if d4[i] == d[j]:
                d6[i] = d6[i]+d[j]
    #print(d6)
    print(sum(d3)+sum(d5))
