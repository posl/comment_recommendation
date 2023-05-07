def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    x = n*m-sum(a)
    print(x if x > 0 else 0 if x <= 0 else -1)

if __name__ == '__main__':
    main()