def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    b=[0]*n
    for i in range(n):
        b[i]=k//n
    k%=n
    for i in range(k):
        b[i]+=1
    c=[0]*n
    for i in range(n):
        c[i]=a[i]
    c.sort()
    for i in range(n):
        for j in range(n):
            if a[i]==c[j]:
                print(b[j])
                break
main()
