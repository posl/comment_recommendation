def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c_a = list(map(int, input().split()))
        c.append(c_a[0])
        a.append(c_a[1:])
    print(c)
    print(a)

if __name__ == '__main__':
    main()