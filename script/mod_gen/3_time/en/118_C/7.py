def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if n==2:
        print(min(a[0],a[1]))
    else:
        for i in range(n-3,-1,-1):
            a[i] = min(a[i],a[i+1]-1)
        print(max(1,a[0]-1))

if __name__ == '__main__':
    main()