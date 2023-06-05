def main():
    n=int(input())
    s=[]
    t=[]
    for i in range(n):
        s.append(list(map(int,input().split())))
    for i in range(n):
        t.append(list(map(int,input().split())))
    #print(s)
    #print(t)
    for i in range(n):
        for j in range(n):
            s1=s.copy()
            t1=t.copy()
            #print(s1)
            #print(t1)
            #print(i)
            #print(j)
            #print(s1[i][0])
            #print(s1[i][1])
            #print(t1[j][0])
            #print(t1[j][1])
            p=(t1[j][0]-s1[i][0],t1[j][1]-s1[i][1])
            #print(p)
            #print(p[0])
            #print(p[1])
            for k in range(n):
                s1[k][0]=s1[k][0]+p[0]
                s1[k][1]=s1[k][1]+p[1]
            #print(s1)
            #print(t1)
            #print(s1[i][0])
            #print(s1[i][1])
            #print(t1[j][0])
            #print(t1[j][1])
            q=(t1[j][0]-s1[i][0],t1[j][1]-s1[i][1])
            #print(q)
            #print(q[0])
            #print(q[1])
            #print(s1)
            #print(t1)
            for k in range(n):
                s1[k][0]=s1[k][0]+q[0]
                s1[k][1]=s1[k][1]+q[1]
            #print(s1)
            #print(t1)
            #print(s1[i][0])
            #print(s1[i][1])
            #print(t1[j][0])
            #print(t1[j][1])
            #print(s1)
            #print(t1)
            #print(s1[i][0])
            #print(s1[i][1])
            #print(t1[j][0])
            #print(t1[j][1])
            #print(s1)
            #print(t1)
            #print(s1[i][0])
            #print(s1[i][1

if __name__ == '__main__':
    main()