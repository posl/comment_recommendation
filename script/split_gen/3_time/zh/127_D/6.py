def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    b=[]
    for i in range(m):
        b.append(list(map(int,input().split())))
    b.sort(key=lambda x:x[1],reverse=True)
    j=0
    for i in range(n):
        if j==m:
            break
        if a[i]<b[j][1]:
            a[i]=b[j][1]
            b[j][0]-=1
            if b[j][0]==0:
                j+=1
        else:
            break
    print(sum(a))
