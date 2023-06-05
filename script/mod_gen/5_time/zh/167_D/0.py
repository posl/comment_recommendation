def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    i = 0
    while b[i] == 0:
        b[i] = 1
        i = a[i] - 1
    c = []
    while b[i] == 1:
        c.append(i)
        b[i] = 2
        i = a[i] - 1
    d = c.index(i)
    if k < d:
        print(c[k] + 1)
    else:
        print(c[(k - d) % (len(c) - d) + d] + 1)

if __name__ == '__main__':
    main()