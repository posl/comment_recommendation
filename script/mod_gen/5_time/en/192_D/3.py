def main():
    X = input()
    M = int(input())
    d = max([int(c) for c in X])
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    def f(n):
        r = 0
        for c in X:
            r = r * n + int(c)
            if r > M:
                return False
        return True
    l = d + 1
    r = 10 ** 18 + 1
    while l + 1 < r:
        m = (l + r) // 2
        if f(m):
            l = m
        else:
            r = m
    print(l - d)
main()

if __name__ == '__main__':
    main()