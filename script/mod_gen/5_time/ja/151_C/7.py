def main():
    n,m=map(int,input().split())
    p=[0]*n
    s=[0]*n
    for i in range(m):
        a,b=input().split()
        a=int(a)
        if s[a-1]=='AC':
            continue
        if b=='AC':
            p[a-1]+=1
            s[a-1]='AC'
        else:
            p[a-1]+=1
    print(sum(p),s.count('AC'))
main()

if __name__ == '__main__':
    main()