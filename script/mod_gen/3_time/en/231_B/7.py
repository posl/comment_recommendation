def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    a.sort()
    b = []
    for i in range(n):
        b.append(a.count(a[i]))
    c = max(b)
    d = b.index(c)
    print(a[d])

if __name__ == '__main__':
    main()