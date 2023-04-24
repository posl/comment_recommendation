Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]
    dp[A][B][C] = 1
    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            for k in range(99, -1, -1):
                if i + j + k == 0:
                    continue
                dp[i][j][k] *= i + j + k
                if i > 0:
                    dp[i - 1][j][k] += dp[i][j][k] * i / (i + j + k)
                if j > 0:
                    dp[i + 1][j - 1][k] += dp[i][j][k] * j / (i + j + k)
                if k > 0:
                    dp[i][j + 1][k - 1] += dp[i][j][k] * k / (i + j + k)
    ans = 0
    for i in range(99):
        for j in range(99):
            for k in range(99):
                if i + j + k == 0:
                    continue
                ans += dp[i][j][k] * (i + j + k)
    print(ans)

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]
    dp[A][B][C] = 1
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 0:
                    continue
                dp[i][j][k] *= (i + j + k)
                if i > 0:
                    dp[i - 1][j][k] += dp[i][j][k]
                if j > 0:
                    dp[i + 1][j - 1][k] += dp[i][j][k]
                if k > 0:
                    dp[i][j + 1][k - 1] += dp[i][j][k]
                dp[i][j][k] /= (i + j + k)
    ans = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 0:
                    continue
                ans += dp[i][j][k] * (i + j + k)
    print(ans)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]
    dp[a][b][c] = 1
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 0:
                    continue
                s = i + j + k
                dp[i][j][k] *= s
                if i > 0:
                    dp[i - 1][j][k] += dp[i][j][k]
                if j > 0:
                    dp[i + 1][j - 1][k] += dp[i][j][k]
                if k > 0:
                    dp[i][j + 1][k - 1] += dp[i][j][k]
    ans = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 0:
                    continue
                s = i + j + k
                ans += dp[i][j][k] / s * (s / (s - 1))
    print(ans)

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    N = A + B + C
    dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    dp[A][B][C] = 1
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            for k in range(N-1, -1, -1):
                if i == 0 and j == 0 and k == 0:
                    continue
                dp[i][j][k] = (i * dp[i+1][j][k] + j * dp[i][j+1][k] + k * dp[i][j][k+1]) / (i + j + k)
                if i > 0:
                    dp[i][j][k] += dp[i-1][j][k] / (i + j + k)
                if j > 0:
                    dp[i][j][k] += dp[i][j-1][k] / (i + j + k)
                if k > 0:
                    dp[i][j][k] += dp[i][j][k-1] / (i + j + k)
                dp[i][j][k] += 1
    print(dp[0][0][0])

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    for i in range(99):
        for j in range(99):
            for k in range(99):
                dp[i][j][k] = (dp[i][j][k] + dp[i+1][j][k] + dp[i][j+1][k] + dp[i][j][k+1] + 3) * (i+j+k) / (i+j+k+3)
    print(dp[A][B][C])

=======
Suggestion 7

def main():
    A, B, C = list(map(int, input().split()))
    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    for a in range(99):
        for b in range(99):
            for c in range(99):
                dp[a][b][c] = 1 + (dp[a+1][b][c] * a + dp[a][b+1][c] * b + dp[a][b][c+1] * c) / (a + b + c)
    print(dp[A][B][C])
main()

=======
Suggestion 8

def main():
    a,b,c=map(int,input().split())
    if a==0 and b==0:
        print(99)
        exit()
    if a==0 and c==0:
        print(99)
        exit()
    if b==0 and c==0:
        print(99)
        exit()
    if a==0:
        print(99)
        exit()
    if b==0:
        print(99)
        exit()
    if c==0:
        print(99)
        exit()
    s=a+b+c
    t=a/s
    u=b/s
    v=c/s
    ans=1+t*2+u*2+v*2+t*u*2+t*v*2+u*v*2
    print(ans)

main()

=======
Suggestion 9

def main():
    A, B, C = map(int, input().split())
    ans = 0
    ans += A * (A + B + C - 1) / (A + B + C) / (A + B + C - 1)
    ans += B * (A + B + C - 1) / (A + B + C) / (A + B + C - 1)
    ans += C * (A + B + C - 1) / (A + B + C) / (A + B + C - 1)
    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    A,B,C = map(int, input().split())
    print(100*(A+B+C-1)/(A+B+C))
