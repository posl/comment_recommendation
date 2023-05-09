def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        b.append(a[i]%200)
    c = []
    for i in range(n):
        c.append(i)
    d = dict()
    for i in range(n):
        if b[i] in d:
            d[b[i]].append(c[i])
        else:
            d[b[i]] = [c[i]]
    for i in range(200):
        if len(d[i])>=2:
            print('Yes')
            print(len(d[i]),end=' ')
            for j in range(len(d[i])):
                print(d[i][j]+1,end=' ')
            print()
            print(len(d[i]),end=' ')
            for j in range(len(d[i])):
                print(d[i][j]+1,end=' ')
            print()
            return
    print('No')

if __name__ == '__main__':
    main()