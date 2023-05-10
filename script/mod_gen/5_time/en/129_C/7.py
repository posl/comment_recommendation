def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N+1)
    b = []
    for i in range(M+1):
        if i == 0:
            b.append(a[i]-1)
        else:
            b.append(a[i]-a[i-1]-1)
    c = []
    for i in range(M+1):
        if b[i] == 0:
            c.append(1)
        elif b[i] == 1:
            c.append(1)
        else:
            c.append(0)
    for i in range(M+1):
        if i == 0:
            pass
        elif i == 1:
            c[i] = c[i-1]
        else:
            c[i] = (c[i-1] + c[i-2]) % 1000000007
    print(c[M])

if __name__ == '__main__':
    main()