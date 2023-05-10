def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = []
    for i in range(m):
        b.append(0)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += a[i] * c[i+j]
    for i in range(m):
        print(b[i], end=" ")
    print(b[m])

if __name__ == '__main__':
    main()