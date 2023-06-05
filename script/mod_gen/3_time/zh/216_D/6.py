def main():
    N,M = map(int,input().split())
    k = []
    a = []
    for i in range(M):
        k.append(int(input()))
        a.append(list(map(int,input().split())))
    #print(k)
    #print(a)
    c = []
    for i in range(M):
        c.append(a[i][0])
    #print(c)
    for i in range(1,N+1):
        if c.count(i) != 2:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()