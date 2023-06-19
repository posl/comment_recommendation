def main():
    n, m = map(int, input().split())
    p = [0 for i in range(n)]
    s = [0 for i in range(n)]
    for i in range(m):
        pi, si = input().split()
        p[int(pi) - 1] += 1
        if si == 'AC':
            s[int(pi) - 1] = 1
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == 1:
            ac += 1
            wa += p[i] - 1
    print(ac, wa)

if __name__ == '__main__':
    main()