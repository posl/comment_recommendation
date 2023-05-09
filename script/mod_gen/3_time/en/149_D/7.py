def main():
    #read input
    n,k=map(int,input().split())
    r,s,p=map(int,input().split())
    t=input()
    #initialize variables
    ans=0
    #process
    for i in range(n):
        if i-k>=0 and t[i]==t[i-k]:
            t=t[:i]+'x'+t[i+1:]
        if t[i]=='r':
            ans+=p
        elif t[i]=='s':
            ans+=r
        elif t[i]=='p':
            ans+=s
    #print answer
    print(ans)
main()

if __name__ == '__main__':
    main()