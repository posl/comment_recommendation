def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        for j in range(i, n):
            b.append(a[i:j + 1])
    for i in range(len(b)):
        b[i].sort()
    c = []
    for i in range(len(b)):
        if len(b[i]) % 2 == 0:
            c.append(b[i][len(b[i]) // 2 - 1])
        else:
            c.append(b[i][len(b[i]) // 2])
    c.sort()
    if len(c) % 2 == 0:
        print(c[len(c) // 2 - 1])
    else:
        print(c[len(c) // 2])

if __name__ == '__main__':
    main()