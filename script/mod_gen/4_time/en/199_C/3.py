def main():
    n = int(input())
    s = input()
    q = int(input())
    l = list(s[:n])
    r = list(s[n:])
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n and b <= n:
                l[a-1], l[b-1] = l[b-1], l[a-1]
            elif a <= n and b > n:
                l[a-1], r[b-n-1] = r[b-n-1], l[a-1]
            elif a > n and b > n:
                r[a-n-1], r[b-n-1] = r[b-n-1], r[a-n-1]
        elif t == 2:
            l, r = r, l
    print(''.join(l + r))

if __name__ == '__main__':
    main()