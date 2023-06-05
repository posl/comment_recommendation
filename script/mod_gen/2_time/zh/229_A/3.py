def main():
    n = 2**20
    q = int(input())
    a = [-1]*n
    for _ in range(q):
        t, x = map(int, input().split())
        x = x % n
        if t == 1:
            while a[x] != -1:
                x += 1
                x = x % n
            a[x] = x
        else:
            print(a[x])

if __name__ == '__main__':
    main()