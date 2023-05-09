def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    # print(a)
    s = set()
    for i in range(n):
        for j in range(i+1,n):
            s.add(a[i]+a[j])
    # print(s)
    s = list(s)
    s.sort()
    # print(s)
    for i in range(len(s)-1,-1,-1):
        if s[i]%d == 0:
            print(s[i])
            return
    print(-1)

if __name__ == '__main__':
    main()