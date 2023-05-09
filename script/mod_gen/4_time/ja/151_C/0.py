def main():
    n, m = map(int, input().split())
    ac = [0 for i in range(n)]
    wa = [0 for i in range(n)]
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1
    ac = sum(ac)
    wa = sum([x * y for x, y in zip(ac, wa)])
    print(ac, wa)

if __name__ == '__main__':
    main()