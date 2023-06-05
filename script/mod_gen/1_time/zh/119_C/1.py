def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10 ** 9
    for i in range(4 ** n):
        mp = 0
        la, lb, lc = 0, 0, 0
        for j in range(n):
            if (i >> (2 * j)) % 4 == 1:
                mp += 10
                if la > 0:
                    mp += abs(l[j] - la)
                la += l[j]
            elif (i >> (2 * j)) % 4 == 2:
                mp += 10
                if lb > 0:
                    mp += abs(l[j] - lb)
                lb += l[j]
            elif (i >> (2 * j)) % 4 == 3:
                mp += 10
                if lc > 0:
                    mp += abs(l[j] - lc)
                lc += l[j]
        if la > 0 and lb > 0 and lc > 0:
            mp += abs(la - a) + abs(lb - b) + abs(lc - c)
            ans = min(ans, mp)
    print(ans)

if __name__ == '__main__':
    main()