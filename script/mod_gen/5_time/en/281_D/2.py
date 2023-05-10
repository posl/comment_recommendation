def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = sum(a[:k])
    if s % d == 0:
        print(s)
        return
    for i in range(n-k):
        s += a[k+i] - a[i]
        if s % d == 0:
            print(s)
            return
    print(-1)

if __name__ == '__main__':
    main()