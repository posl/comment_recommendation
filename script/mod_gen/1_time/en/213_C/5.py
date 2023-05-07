def main():
    h, w, n = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a = sorted(a)
    b = sorted(b)
    for i in range(n):
        print(a.index(a[i]) + 1, b.index(b[i]) + 1)

if __name__ == '__main__':
    main()