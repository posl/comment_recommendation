def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    for i in range(n):
        if a[i] != 0:
            a[a[i]-1] = 0
    print(n - a.count(0))

if __name__ == '__main__':
    main()