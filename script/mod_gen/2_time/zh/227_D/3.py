def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if k >= n:
        print(0)
        exit()
    else:
        print(a[k-1])

if __name__ == '__main__':
    main()