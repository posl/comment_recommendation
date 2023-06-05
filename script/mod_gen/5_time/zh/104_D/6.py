def main():
    s=input()
    n=len(s)
    mod=10**9+7
    a=[0]*(n+1)
    b=[0]*(n+1)
    c=[0]*(n+1)
    q=0
    for i in range(n):
        if s[i]=="A":
            a[i+1]=a[i]+pow(3,q,mod)
        elif s[i]=="B":
            b[i+1]=b[i]+pow(3,q,mod)
        elif s[i]=="C":
            c[i+1]=c[i]+pow(3,q,mod)
        else:
            a[i+1]=a[i]*3+pow(3,q,mod)
            b[i+1]=b[i]*3+a[i]
            c[i+1]=c[i]*3+b[i]
            q+=1
    print(c[n]%mod)

if __name__ == '__main__':
    main()