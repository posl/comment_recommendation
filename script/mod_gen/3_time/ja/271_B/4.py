def main():
    n,q=map(int,input().split())
    a=[[] for _ in range(n)]
    for i in range(n):
        a[i]=list(map(int,input().split()))
    for i in range(q):
        s,t=map(int,input().split())
        print(a[s-1][t-1])

if __name__ == '__main__':
    main()