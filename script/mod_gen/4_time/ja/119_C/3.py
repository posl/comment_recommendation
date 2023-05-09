def main():
    import sys
    input = sys.stdin.readline
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    INF = 10 ** 9
    ans = INF
    for i in range(4 ** N):
        a = []
        b = []
        c = []
        for j in range(N):
            if (i >> (2 * j)) & 3 == 0:
                a.append(L[j])
            elif (i >> (2 * j)) & 3 == 1:
                b.append(L[j])
            elif (i >> (2 * j)) & 3 == 2:
                c.append(L[j])
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            continue
        mp = 0
        mp += (len(a) - 1) * 10
        mp += (len(b) - 1) * 10
        mp += (len(c) - 1) * 10
        mp += abs(sum(a) - A)
        mp += abs(sum(b) - B)
        mp += abs(sum(c) - C)
        ans = min(ans, mp)
    print(ans)

if __name__ == '__main__':
    main()