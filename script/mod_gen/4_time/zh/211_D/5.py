def main():
    n,m=map(int,input().split())
    ab=[list(map(int,input().split())) for _ in range(m)]
    ab.sort(key=lambda x:x[1])
    last=0
    ans=0
    for a,b in ab:
        if a>last:
            last=b-1
            ans+=1
    print(ans)

if __name__ == '__main__':
    main()