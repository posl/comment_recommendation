def main():
    N = int(input())
    MOD = 10**9+7
    # AGC, ACG, GAC, AC, AG, GC
    # 0, 1, 2, 3, 4, 5
    dp = [[[[[0]*6 for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(N+1)]
    dp[0][5][5][5][5] = 1
    for i in range(N):
        for a in range(6):
            for b in range(6):
                for c in range(6):
                    for d in range(6):
                        for e in range(6):
                            if dp[i][a][b][c][d] == 0:
                                continue
                            for f in range(6):
                                if (a == 3 and b == 0 and f == 1) or (a == 3 and c == 0 and f == 1) or (b == 3 and c == 0 and f == 1) or (a == 3 and d == 0 and f == 1) or (b == 3 and d == 0 and f == 1) or (c == 3 and d == 0 and f == 1):
                                    continue
                                if (a == 4 and b == 0 and f == 2) or (a == 4 and c == 0 and f == 2) or (b == 4 and c == 0 and f == 2) or (a == 4 and d == 0 and f == 2) or (b == 4 and d == 0 and f == 2) or (c == 4 and d == 0 and f == 2) or (d == 4 and e == 0 and f == 2):
                                    continue
                                if (a == 5 and b == 0 and f == 3) or (a == 5 and c == 0 and f == 3) or (b == 5 and c == 0 and f == 3) or (a == 5 and d == 0 and f == 3) or (b == 5 and d == 0 and f == 3)
