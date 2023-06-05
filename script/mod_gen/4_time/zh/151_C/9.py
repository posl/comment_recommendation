def main():
    n, m = map(int, input().split())
    p = [0]*n
    s = [0]*n
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        if s[pi-1] == 0:
            s[pi-1] = si
            if si == 'AC':
                ac[pi-1] = 1
            else:
                wa[pi-1] = 1
    print(sum(ac), sum([ac[i]*wa[i] for i in range(n)]))

if __name__ == '__main__':
    main()