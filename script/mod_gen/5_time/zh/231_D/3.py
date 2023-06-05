def main():
    n,m = map(int,input().split())
    if m == 0:
        print('No')
    else:
        a = []
        b = []
        for i in range(m):
            a1,b1 = map(int,input().split())
            a.append(a1)
            b.append(b1)
        a.sort()
        b.sort()
        if b[0] - a[-1] == 1:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()