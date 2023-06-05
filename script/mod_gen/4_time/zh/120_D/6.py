def main():
    n,m = map(int,input().split())
    a = [0 for _ in range(m)]
    b = [0 for _ in range(m)]
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    print(n,m,a,b)

if __name__ == '__main__':
    main()