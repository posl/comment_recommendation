def main():
    n, m = map(int, input().split())
    ac = [0] * (n + 1)
    wa = [0] * (n + 1)
    for _ in range(m):
        p, s = input().split()
        p = int(p)
        if ac[p] == 0:
            if s == 'AC':
                ac[p] = 1
            else:
                wa[p] += 1
    print(sum(ac), sum(wa[i] if ac[i] else 0 for i in range(n + 1)))

if __name__ == '__main__':
    main()