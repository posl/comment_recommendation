def main():
    n,m=map(int,input().split())
    a=[list(map(int,input().split())) for i in range(m)]
    ans="No"
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(m):
                if i in a[k] and j in a[k]:
                    ans="Yes"
                    break
    print(ans)

if __name__ == '__main__':
    main()