def check(x,y,z,w):
    global a
    p=sum(a[x:y])
    q=sum(a[y:z])
    r=sum(a[z:w])
    if p==q and q==r:
        return True
    else:
        return False
n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n-3):
    for j in range(i+1,n-2):
        for k in range(j+1,n-1):
            for l in range(k+1,n):
                if check(i,j,k,l):
                    print('Yes')
                    exit()
print('No')

if __name__ == '__main__':
    check()