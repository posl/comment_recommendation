def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if K >= N:
        for i in range(N):
            print(K//N)
    else:
        b = []
        for i in range(N):
            b.append([a[i],i])
        b.sort()
        c = K
        for i in range(N):
            if b[i][1] < c:
                print(K//N + 1)
            else:
                print(K//N)
        #print(b)

if __name__ == '__main__':
    main()