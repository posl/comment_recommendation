def main():
    n, m = map(int, input().split())
    ac = [False] * n
    wa = [0] * n
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if ac[p]:
            continue
        if s == 'AC':
            ac[p] = True
        else:
            wa[p] += 1
    print(sum(ac), sum([w if ac[i] else 0 for i, w in enumerate(wa)]))

if __name__ == '__main__':
    main()