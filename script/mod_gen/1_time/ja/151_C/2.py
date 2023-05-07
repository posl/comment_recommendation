def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        pi = int(pi) - 1
        if s[pi] == 0:
            if si == 'AC':
                p[pi] = 1
            else:
                s[pi] += 1
        else:
            if si == 'AC':
                continue
            else:
                s[pi] += 1
    print(sum(p), sum([s[i] * p[i] for i in range(n)]))

if __name__ == '__main__':
    main()