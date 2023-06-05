def main():
    n,m=map(int,input().split())
    if m==0:
        print(1)
        return
    mlist=list(map(int,input().split()))
    mlist.sort()
    klist=[]
    for i in range(m-1):
        klist.append(mlist[i+1]-mlist[i])
    klist.sort()
    k=klist[0]
    count=0
    for i in range(m):
        count+=((mlist[i]-1)//k)
        if (mlist[i]-1)%k!=0:
            count+=1
    count+=((n-mlist[m-1])//k)
    if (n-mlist[m-1])%k!=0:
        count+=1
    print(count)
    return
main()
