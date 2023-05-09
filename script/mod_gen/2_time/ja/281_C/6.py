def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    total = sum(a)
    q,r = divmod(t,total)
    ans = 0
    for i in range(n):
        r -= a[i]
        if r < 0:
            ans = i+1
            break
    print(ans,r+a[i])

if __name__ == '__main__':
    main()