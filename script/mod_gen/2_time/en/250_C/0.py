def main():
    n, q = map(int, input().split())
    a = list(range(1, n + 1))
    for i in range(q):
        x = int(input())
        a[x - 1], a[x] = a[x], a[x - 1]
    print(' '.join(map(str, a)))
main()

if __name__ == '__main__':
    main()