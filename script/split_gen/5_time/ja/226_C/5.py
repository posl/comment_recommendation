def readinput():
    n=int(input())
    t=[]
    a=[]
    for _ in range(n):
        line=input().split()
        t.append(int(line[0]))
        a.append([int(line[2+i])-1 for i in range(int(line[1]))])
    return n,t,a
