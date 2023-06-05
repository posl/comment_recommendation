def main():
    n, q = map(int, input().split())
    x = []
    for i in range(q):
        x.append(int(input()))
    #print(x)
    a = [i for i in range(1, n+1)]
    #print(a)
    for i in range(q):
        #print(x[i])
        #print(a)
        #print(a.index(x[i]))
        tmp = a.index(x[i])
        #print(tmp)
        if tmp != n-1:
            a[tmp], a[tmp+1] = a[tmp+1], a[tmp]
        else:
            a[tmp], a[tmp-1] = a[tmp-1], a[tmp]
    #print(a)
    print(*a)

if __name__ == '__main__':
    main()