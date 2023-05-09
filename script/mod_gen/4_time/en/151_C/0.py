def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        _p, _s = input().split()
        p.append(int(_p))
        s.append(_s)
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        else:
            wa += 1
    print(ac, wa)

if __name__ == '__main__':
    main()