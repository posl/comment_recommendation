def main():
    n=int(input())
    s=input()
    w=list(map(int,input().split()))
    w1=[w[i] for i in range(n) if s[i]=='1']
    w0=[w[i] for i in range(n) if s[i]=='0']
    w1.sort()
    w0.sort()
    w0.reverse()
    ans=0
    for i in range(1,len(w1)+1):
        j=len(w0)-i
        if j>=0:
            ans=max(ans,sum(w1[:i])+sum(w0[:j]))
        else:
            ans=max(ans,sum(w1[:i]))
    print(ans)

if __name__ == '__main__':
    main()