def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if m*n - sum(a) > k:
        print(-1)
    else:
        print(max(0,m*n-sum(a)))

if __name__ == '__main__':
    main()