def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort(reverse=True)
    x.sort(reverse=True)
    ans = 0
    for i in range(min(n,q)):
        if a[i] > x[i]:
            ans += a[i] - x[i]
        else:
            break
    if q > n:
        ans += sum(x[n:])
    print(ans)

if __name__ == '__main__':
    main()