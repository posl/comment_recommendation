def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int,input().split()))
    a.sort()
    white = []
    for i in range(m):
        if i == 0:
            white.append(a[i]-1)
        else:
            white.append(a[i]-a[i-1]-1)
        if i == m-1:
            white.append(n-a[i])
    white.sort()
    if white[0] == 0:
        print(0)
        return
    k = white[0]
    count = 0
    for i in range(m):
        count += (a[i]+k-1)//k
    print(count)

if __name__ == '__main__':
    main()