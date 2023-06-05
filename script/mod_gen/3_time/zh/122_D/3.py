def main():
    N = int(input())
    mod = 10 ** 9 + 7
    S = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                S[3][c1][c2][c3] = 1
    for n in range(4, N + 1):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for c4 in range(4):
                        if c2 == 0 and c3 == 2 and c4 == 1:
                            continue
                        if c2 == 2 and c3 == 0 and c4 == 1:
                            continue
                        if c2 == 0 and c3 == 1 and c4 == 2:
                            continue
                        if c1 == 0 and c3 == 2 and c4 == 1:
                            continue
                        if c1 == 0 and c2 == 2 and c4 == 1:
                            continue
                        S[n][c2][c3][c4] += S[n - 1][c1][c2][c3]
                        S[n][c2][c3][c4] %= mod
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += S[N][c1][c2][c3]
                ans %= mod
    print(ans)

if __name__ == '__main__':
    main()