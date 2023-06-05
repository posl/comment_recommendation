def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i = 0
    for x in a:
        while i+1 < m and b[i+1] < x:
            i += 1
        ans = min(ans,abs(x-b[i]))
        if i+1 < m:
            ans = min(ans,abs(x-b[i+1]))
    print(ans)

if __name__ == '__main__':
    main()