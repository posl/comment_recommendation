def main():
    N = int(input())
    MOD = 1000000007
    s = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                if c1 == 0 and c2 == 1 and c3 == 2:
                    continue
                if c1 == 0 and c2 == 2 and c3 == 1:
                    continue
                if c1 == 1 and c2 == 0 and c3 == 2:
                    continue
                s[3][c1][c2][c3] = 1
    for i in range(4, N+1):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for c4 in range(4):
                        if c2 == 0 and c3 == 1 and c4 == 2:
                            continue
                        if c2 == 0 and c3 == 2 and c4 == 1:
                            continue
                        if c1 == 0 and c3 == 1 and c4 == 2:
                            continue
                        if c1 == 0 and c2 == 1 and c4 == 2:
                            continue
                        if c1 == 0 and c2 == 1 and c3 == 2:
                            continue
                        s[i][c2][c3][c4] += s[i-1][c1][c2][c3]
                        s[i][c2][c3][c4] %= MOD
    ans = 0
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                ans += s[N][c1][c2][c3]
                ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()