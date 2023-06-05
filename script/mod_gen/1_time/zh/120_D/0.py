def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    print(a)
    print(b)
    print('------------------')
    for i in range(m):
        print(i)
        print('a[:i]',a[:i])
        print('b[:i]',b[:i])
        print('a[i+1:]',a[i+1:])
        print('b[i+1:]',b[i+1:])
        print('------------------')
        print(len(set(a[:i])|set(b[:i])))
        print(len(set(a[i+1:])|set(b[i+1:])))
        print(len(set(a[:i])|set(b[:i]))*len(set(a[i+1:])|set(b[i+1:])))
        print('------------------')
        print(len(set(a[:i])|set(b[:i]))*len(set(a[i+1:])|set(b[i+1:]))-len(set(a[:i])|set(b[:i]))*len(set(a[i+1:])|set(b[i+1:])))
        print('------------------')
        print('------------------')
        print('------------------')

if __name__ == '__main__':
    main()