def main():
    n,q=map(int,input().split())
    s=input()
    ac=[0]*(n+1)
    for i in range(1,n):
        ac[i+1]=ac[i]
        if s[i-1:i+1]=="AC":
            ac[i+1]+=1
    for i in range(q):
        l,r=map(int,input().split())
        print(ac[r]-ac[l])

if __name__ == '__main__':
    main()