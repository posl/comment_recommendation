def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = []
    for i in range(n):
        for j in range(i, n):
            b.append(a[i:j+1])
    c = []
    for i in range(len(b)):
        b[i].sort()
        c.append(b[i][int((len(b[i])-1)/2)])
    c.sort()
    print(c[int((len(c)-1)/2)])

if __name__ == '__main__':
    main()