def main():
    s,k=map(str,input().split())
    k=int(k)
    s=list(s)
    s.sort()
    count=0
    while count<k-1:
        i=len(s)-1
        while i>0 and s[i-1]>=s[i]:
            i-=1
        j=len(s)-1
        while s[j]<=s[i-1]:
            j-=1
        s[i-1],s[j]=s[j],s[i-1]
        s[i:]=s[len(s)-1:i-1:-1]
        count+=1
    print("".join(s))

if __name__ == '__main__':
    main()