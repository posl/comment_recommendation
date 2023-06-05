def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    c.sort(reverse=True)
    sum = 0
    for i in range(0, n, 2):
        sum += c[i]
    print(sum)

if __name__ == '__main__':
    main()