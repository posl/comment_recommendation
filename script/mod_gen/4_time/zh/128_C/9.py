def main():
    n,m=map(int,input().split())
    k=[]
    s=[]
    p=[]
    for i in range(m):
        k.append(list(map(int,input().split()))[0])
        s.append(list(map(int,input().split())))
    p=list(map(int,input().split()))
    count=0
    for i in range(2**n):
        flag=True
        for j in range(m):
            sum=0
            for l in range(k[j]):
                sum+=((i>>(s[j][l]-1))&1)
            if sum%2!=p[j]:
                flag=False
                break
        if flag:
            count+=1
    print(count)

if __name__ == '__main__':
    main()