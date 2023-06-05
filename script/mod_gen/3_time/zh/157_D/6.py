def main():
    n,m,k = map(int,input().split())
    a = [0] * m
    b = [0] * m
    c = [0] * k
    d = [0] * k
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(k):
        c[i],d[i] = map(int,input().split())
    print(a,b,c,d)
    for i in range(1,n+1):
        cnt = 0
        for j in range(m):
            if a[j] == i:
                cnt += 1
            if b[j] == i:
                cnt += 1
        for j in range(k):
            if c[j] == i:
                cnt -= 1
            if d[j] == i:
                cnt -= 1
        print(cnt,end=' ')
    print()

if __name__ == '__main__':
    main()