def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[i] = a[i]
        else:
            b[i] = -a[i]
    c = [0] * n
    for i in range(n):
        if i % 2 == 0:
            c[i] = -a[i]
        else:
            c[i] = a[i]
    print(max(sum(b), sum(c)))

if __name__ == '__main__':
    main()