def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))
    snuke.sort()
    t, x, a = snuke[0]
    if x == 0:
        ans = a
    else:
        ans = 0
    for i in range(1, n):
        t1, x1, a1 = snuke[i]
        if t1 - t >= abs(x1 - x):
            ans += a1
            t, x, a = t1, x1, a1
        elif x1 > x:
            ans += a1 - (abs(x1 - x) - (t1 - t))
            t, x, a = t1, x1, a1
    print(ans)

if __name__ == '__main__':
    main()