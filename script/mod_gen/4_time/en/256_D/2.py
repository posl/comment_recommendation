def main():
    n = int(input())
    a = []
    for i in range(n):
        l,r = map(int,input().split())
        a.append([l,r])
    a.sort()
    l = a[0][0]
    r = a[0][1]
    for i in range(1,n):
        if a[i][0] <= r:
            r = max(r,a[i][1])
        else:
            print(l,r)
            l = a[i][0]
            r = a[i][1]
    print(l,r)
main()

if __name__ == '__main__':
    main()