def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10 ** 9
    ans = INF
    for i in range(4 ** N):
        A1 = 0
        B1 = 0
        C1 = 0
        mp = 0
        for j in range(N):
            if (i >> 2 * j) & 3 == 1:
                if A1 != 0:
                    mp += 10
                A1 += l[j]
            elif (i >> 2 * j) & 3 == 2:
                if B1 != 0:
                    mp += 10
                B1 += l[j]
            elif (i >> 2 * j) & 3 == 3:
                if C1 != 0:
                    mp += 10
                C1 += l[j]
        if A1 != 0 and B1 != 0 and C1 != 0:
            mp += abs(A1 - A) + abs(B1 - B) + abs(C1 - C)
            ans = min(ans, mp)
    print(ans)

if __name__ == '__main__':
    main()