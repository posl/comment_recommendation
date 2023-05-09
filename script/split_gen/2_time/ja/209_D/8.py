def main():
    N,Q=map(int,input().split())
    #print(N,Q)
    #N=4
    #Q=1
    #a=[1,2,2,4]
    #b=[2,3,4,1]
    #c=[1,2]
    #d=[2,1]
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(N-1):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(Q):
        x,y=map(int,input().split())
        c.append(x)
        d.append(y)
    #print(a,b,c,d)
    #print(a,b)
    #print(c,d)
    #pri
