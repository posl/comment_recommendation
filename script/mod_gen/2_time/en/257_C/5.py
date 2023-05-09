def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    # 0: child, 1: adult
    s = [int(x) for x in s]
    # 0: child, 1: adult
    w = [(x, i) for i, x in enumerate(w)]
    w.sort()
    # 0: child, 1: adult
    s = [s[x[1]] for x in w]
    # 0: child, 1: adult
    c = [0] * n
    a = [0] * n
    # 0: child, 1: adult
    c[0] = 1 - s[0]
    a[0] = s[0]
    for i in range(1, n):
        c[i] = c[i - 1] + 1 - s[i]
        a[i] = a[i - 1] + s[i]
    ans = 0
    for i in range(n):
        ans = max(ans, c[i] + a[n - 1] - a[i])
    print(ans)

if __name__ == '__main__':
    main()