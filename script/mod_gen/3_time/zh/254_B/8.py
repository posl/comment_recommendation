def test():
    n = 10
    a = []
    for i in range(n):
        b = []
        for j in range(i+1):
            if j == 0 or j == i:
                b.append(1)
            else:
                b.append(a[i-1][j-1] + a[i-1][j])
        a.append(b)
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
    return 0

if __name__ == '__main__':
    test()