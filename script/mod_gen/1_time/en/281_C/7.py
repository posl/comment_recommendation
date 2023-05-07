def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    c = t // s
    r = t % s
    a = a * 2
    for i in range(2 * n):
        r -= a[i]
        if r < 0:
            print(i + 1, -r)
            break

if __name__ == '__main__':
    main()