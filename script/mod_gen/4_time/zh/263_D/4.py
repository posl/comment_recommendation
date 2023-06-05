def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        if a[i] < 0:
            sum += a[i]*(l+r)
        else:
            sum += a[i]*(l-r)
    print(sum)

if __name__ == '__main__':
    main()