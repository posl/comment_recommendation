def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0]*(m+1)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += c[i]*a[n-i]
    print(" ".join(map(str,b)))

if __name__ == '__main__':
    main()