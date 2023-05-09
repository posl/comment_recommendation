def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if t == total:
        print(n, 0)
        return
    t = t % total
    for i in range(n):
        if t < a[i]:
            print(i + 1, t)
            return
        t -= a[i]

if __name__ == '__main__':
    main()