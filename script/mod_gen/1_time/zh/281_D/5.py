def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    s = set()
    for i in range(n):
        for j in range(i+1,n):
            s.add(a[i]+a[j])
    s = list(s)
    s.sort()
    for i in range(len(s)-1,-1,-1):
        if s[i]%d == 0:
            print(s[i])
            break
        elif i == 0:
            print(-1)

if __name__ == '__main__':
    main()