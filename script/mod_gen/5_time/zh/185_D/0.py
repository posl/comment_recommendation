def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int,input().split()))
    a.sort()
    if a[0] != 1:
        a.insert(0,0)
    if a[-1] != n:
        a.append(n+1)
    k = n
    for i in range(len(a)-1):
        if a[i+1] - a[i] - 1 > 0:
            k = min(k,a[i+1] - a[i] - 1)
    ans = 0
    for i in range(len(a)-1):
        ans += (a[i+1] - a[i] - 1) // k
        if (a[i+1] - a[i] - 1) % k != 0:
            ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()