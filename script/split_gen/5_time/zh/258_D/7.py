def main():
    n,x=map(int,input().split())
    ab=[]
    for i in range(n):
        ab.append(list(map(int,input().split())))
    a,b=zip(*ab)
    a=list(a)
    b=list(b)
    #print(a)
    #print(b)
    time=[]
    for i in range(n):
        time.append(a[i]+b[i])
    #print(time)
    #print(sum(time))
    #print(x)
    #print(sum(time)/x)
    if sum(time)<=x:
        print(n)
    else:
        time.sort()
        #print(time)
        #print(sum(time))
        #print(x)
        count=0
        for i in time:
            if x>=i:
                count+=1
                x-=i
            else:
                break
        print(count)
main()
