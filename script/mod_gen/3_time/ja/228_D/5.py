def main():
    n = 2**20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        x %= n
        if t == 1:
            while a[x] != -1:
                x += 1
                x %= n
            a[x] = x
        else:
            print(a[x])

if __name__ == '__main__':
    main()