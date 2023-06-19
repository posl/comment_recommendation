def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if m == 0:
        print(1)
        return
    a.sort()
    # print(a)
    # print(n, m)
    # print(a)
    if a[0] != 1:
        a.insert(0, 0)
    if a[-1] != n:
        a.append(n+1)
    # print(a)
    b = []
    for i in range(len(a)-1):
        if a[i+1] - a[i] > 1:
            b.append(a[i+1] - a[i] - 1)
    # print(b)
    if len(b) == 0:
        print(0)
        return
    k = min(b)
    ans = 0
    for i in b:
        ans += (i+k-1)//k
    print(ans)

if __name__ == '__main__':
    main()