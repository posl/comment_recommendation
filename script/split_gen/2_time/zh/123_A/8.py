def main():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for c1 in "ACGT":
            for c2 in "ACGT":
                for c3 in "ACGT":
                    if c2 == "A" and c3 == "G" and c1 == "C":
                        continue
                    if c2 == "G" and c3 == "A" and c1 == "C":
                        continue
                    if c2 == "A" and c3 == "C" and c1 == "G":
                        continue
                    if c2 == "A" and c3 == "G" and c1 == "C":
                        continue
                    if c2 == "A" and c3 == "C" and c1 == "A":
                        continue
                    dp[i] += dp[i - 1]
                    dp[i] %= 1000000007
    print(dp[N])
