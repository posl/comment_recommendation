def main():
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    print(l[k-1])

if __name__ == '__main__':
    main()