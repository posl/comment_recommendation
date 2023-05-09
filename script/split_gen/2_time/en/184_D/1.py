def main():
    A, B, C = map(int, input().split())
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]
    dp[A][B][C] = 1
    for a in range(A, -1, -1):
        for b in range(B, -1, -1):
            for c in range(C, -1, -1):
                if a + b + c == 0:
                    continue
                tot = a + b + c
                dp[a][b][c] *= tot
                dp[a][b][c] += dp[a + 1][b][c] * a
                dp[a][b][c] += dp[a][b + 1][c] * b
                dp[a][b][c] += dp[a][b][c + 1] * c
                dp[a][b][c] /= tot
    ans = 0
    for a in range(1, A + 1):
        ans += dp[a][0][0]
    for b in range(1, B + 1):
        ans += dp[0][b][0]
    for c in range(1, C + 1):
        ans += dp[0][0][c]
    print(ans)
main()
We have a bag containing A gold coins, B silver coins, and C bronze coins.
Until the bag contains 100 coins of the same color, we will repeat the following operation:
Operation: Randomly take out one coin from the bag. (Every coin has an equal probability of being chosen.) Then, put back into the bag two coins of the same kind as the removed coin.
Find the expected value of the number of times the operation is done.
Constraints
0 ≦ A,B,C ≦ 99
A+B+C ≧ 1
Input
Input is given from Standard Input in the following format:
A B C
Output
Print the expected value of the number of times the operation is done. Your output will be accepted if its absolute or relative error from the correct value is at most 10^{-6}.
Sample Input 1
99 99 99
Sample Output 1
1.000000000
No matter what coin we take out in the first operation, the bag will contain 100 coins of that kind.
Sample
