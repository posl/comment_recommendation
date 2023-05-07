def main():
    n,m=map(int,input().split())
    p=[0]*n
    s=[0]*n
    for i in range(m):
        pp,ss=input().split()
        p[int(pp)-1]=int(pp)
        s[int(pp)-1]=ss
    #print(p)
    #print(s)
    ac=0
    wa=[0]*n
    for i in range(m):
        if s[i]=='AC':
            if wa[p[i]-1]==0:
                ac+=1
                wa[p[i]-1]=1
        else:
            if wa[p[i]-1]==0:
                wa[p[i]-1]=2
    #print(wa)
    wa2=0
    for i in range(n):
        if wa[i]==2:
            wa2+=1
    print(ac,wa2)
