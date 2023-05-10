def main():
    n, m = map(int, input().split())
    k = [0] * n
    a = [0] * n
    for i in range(n):
        k[i], *a[i] = map(int, input().split())
    s = set(a[0])
    for i in range(1, n):
        s &= set(a[i])
    print(len(s))

if __name__ == '__main__':
    main()