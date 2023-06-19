def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]
    for i in range(n):
        b.append(b[i]+a[i])
    maxv = -float('inf')
    for i in range(n-m+1):
        maxv = max(maxv,b[i+m]-b[i])
    print(maxv)

if __name__ == '__main__':
    main()