def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n, 0, -1):
        c = 0
        for j in range(i, n + 1, i):
            c += b[j - 1]
        if c % 2 != a[i - 1]:
            b.append(1)
        else:
            b.append(0)
    print(sum(b))
    for k in range(len(b)):
        if b[k] == 1:
            print(k + 1, end=' ')
    print()

if __name__ == '__main__':
    main()