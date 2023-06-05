def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n*m-sum(a) <= k and n*m-sum(a) >= 0:
        print(n*m-sum(a))
    else:
        print(-1)

if __name__ == '__main__':
    main()