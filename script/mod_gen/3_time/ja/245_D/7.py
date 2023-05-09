def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = []
    for i in range(n+m+1):
        b.append(0)
    for i in range(n+1):
        for j in range(m+1):
            b[i+j] += a[i]*c[j]
    for i in range(m+1):
        print(b[i],end=" ")

if __name__ == '__main__':
    main()