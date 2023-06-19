def main():
    N, M = map(int, input().split())
    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            AC[p - 1] = 1
        else:
            if AC[p - 1] == 0:
                WA[p - 1] += 1
    print(sum(AC), sum([x * y for x, y in zip(AC, WA)]))

if __name__ == '__main__':
    main()