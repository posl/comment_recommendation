def main():
    n = int(input())
    mod = 10**9 + 7
    dp = [{} for _ in range(n+1)]
    dp[0][('T', 'T', 'T')] = 1
    for i in range(n):
        for (a, b, c), v in dp[i].items():
            for x in 'ACGT':
                if b == 'A' and c == 'G' and x == 'C': continue
                if b == 'G' and c == 'A' and x == 'C': continue
                if b == 'A' and c == 'C' and x == 'G': continue
                if a == 'A' and c == 'G' and x == 'C': continue
                if a == 'A' and b == 'G' and x == 'C': continue
                if b == 'A' and c == 'G' and x == 'T': continue
                if b == 'A' and c == 'T' and x == 'G': continue
                if a == 'A' and b == 'G' and x == 'T': continue
                if a == 'G' and b == 'A' and x == 'C': continue
                if a == 'A' and b == 'C' and x == 'G': continue
                dp[i+1][(b, c, x)] = (dp[i+1].get((b, c, x), 0) + v) % mod
    print(sum(dp[n].values()) % mod)
