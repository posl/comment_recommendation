def main():
    n = int(input())
    a = [-1] * (2 ** 20)
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % (2 ** 20)] != -1:
                h += 1
            a[h % (2 ** 20)] = x
        else:
            print(a[x % (2 ** 20)])

if __name__ == '__main__':
    main()