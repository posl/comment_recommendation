def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        if s[pi] == 0:
            if si == 'AC':
                p[pi] += 1
            else:
                s[pi] += 1
        else:
            continue
    ac = 0
    wa = 0
    for i in range(1, n + 1):
        if p[i] > 0:
            ac += 1
            wa += s[i]
    print(ac, wa)

if __name__ == '__main__':
    main()