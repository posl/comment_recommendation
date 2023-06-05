def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for c1 in "ACGT":
            for c2 in "ACGT":
                for c3 in "ACGT":
                    if c1 == "A" and c2 == "G" and c3 == "C":
                        continue
                    if c1 == "A" and c2 == "C" and c3 == "G":
                        continue
                    if c1 == "G" and c2 == "A" and c3 == "C":
                        continue
                    if c1 == "A" and c2 == "G" and c3 == "T":
                        continue
                    if c1 == "A" and c2 == "T" and c3 == "G":
                        continue
                    if c1 == "G" and c2 == "A" and c3 == "T":
                        continue
                    if c1 == "G" and c2 == "T" and c3 == "A":
                        continue
                    if c1 == "T" and c2 == "G" and c3 == "A":
                        continue
                    if c1 == "C" and c2 == "G" and c3 == "A":
                        continue
                    if c1 == "G" and c2 == "C" and c3 == "A":
                        continue
                    dp[i] += dp[i - 1]
                    dp[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()