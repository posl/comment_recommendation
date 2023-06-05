def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    print(sum(a[0:k]))

if __name__ == '__main__':
    main()