def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = [i%200 for i in a]
    d = dict()
    for i in range(1,1<<n):
        s = 0
        b = []
        for j in range(n):
            if i&(1<<j):
                s += a[j]
                b.append(j+1)
        if s%200 in d:
            print('Yes')
            print(len(d[s%200]),*d[s%200])
            print(len(b),*b)
            return
        else:
            d[s%200] = b
    print('No')

if __name__ == '__main__':
    main()