def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        x = i
        s = 0
        l = 0
        while True:
            x = p[x] - 1
            s += c[x]
            l += 1
            if x == i:
                break
            if l == k:
                break
        if s > 0:
            t = (k // l - 1) * s
            x = i
            u = 0
            while True:
                x = p[x] - 1
                u += c[x]
                if x == i:
                    break
                t = max(t, u)
            ans = max(ans, t)
        else:
            ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    main()