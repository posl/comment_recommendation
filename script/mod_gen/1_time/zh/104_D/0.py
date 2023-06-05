def main():
    s=input()
    n=len(s)
    q=s.count("?")
    ans=0
    for i in range(n):
        if s[i]=="B" or s[i]=="?":
            ans+=pow(3,q,1000000007)*pow(3,i,1000000007)
            q-=1
        if s[i]=="C" or s[i]=="?":
            ans+=pow(3,q,1000000007)*pow(3,i,1000000007)
            q-=1
    print(ans%1000000007)

if __name__ == '__main__':
    main()