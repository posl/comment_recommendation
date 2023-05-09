def main():
    n = 2 ** 20
    a = [-1] * n
    q = int(input())
    for i in range(q):
        t, x = map(int, input().split())
        h = x
        if t == 1:
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])

if __name__ == '__main__':
    main()