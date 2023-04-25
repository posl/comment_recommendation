Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())

    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    dp[A][B][C] = 1

    for a in range(100):
        for b in range(100):
            for c in range(100):
                if a == 0 and b == 0 and c == 0:
                    continue
                total = a + b + c
                dp[a][b][c] += a / total * dp[max(0, a - 1)][b][c]
                dp[a][b][c] += b / total * dp[a][max(0, b - 1)][c]
                dp[a][b][c] += c / total * dp[a][b][max(0, c - 1)]
                dp[a][b][c] *= total / (total + 1)
                dp[a][b][c] += 1

    ans = 0
    for a in range(100):
        for b in range(100):
            for c in range(100):
                if a == 0 and b == 0 and c == 0:
                    continue
                total = a + b + c
                ans += dp[a][b][c] * a / total
                ans += dp[a][b][c] * b / total
                ans += dp[a][b][c] * c / total

    print(ans)

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if A == 0 and B == 0:
        print(99)
        return
    if A == 0 and C == 0:
        print(99)
        return
    if B == 0 and C == 0:
        print(99)
        return
    print(1 + A / (A + B + C) * (1 + B / (A + B + C - 1) * (1 + C / (A + B + C - 2))) + B / (A + B + C) * (1 + A / (A + B + C - 1) * (1 + C / (A + B + C - 2))) + C / (A + B + C) * (1 + A / (A + B + C - 1) * (1 + B / (A + B + C - 2))))

main()

=======
Suggestion 3

def main():
    A,B,C = map(int, input().split())
    dp = [[[0.0 for _ in range(200)] for _ in range(200)] for _ in range(200)]
    dp[A][B][C] = 1.0
    ans = 0.0
    for i in range(A+1):
        for j in range(B+1):
            for k in range(C+1):
                if i+j+k == 0:
                    continue
                if i+j+k == 100:
                    ans += dp[i][j][k]
                    continue
                if i > 0:
                    dp[i-1][j+1][k+1] += dp[i][j][k] * i / (i+j+k)
                if j > 0:
                    dp[i+1][j-1][k+1] += dp[i][j][k] * j / (i+j+k)
                if k > 0:
                    dp[i+1][j+1][k-1] += dp[i][j][k] * k / (i+j+k)
    print(ans)

=======
Suggestion 4

def main():
    A,B,C = map(int, input().split())
    X = A+B+C
    dp = [[[0 for _ in range(X+1)] for _ in range(X+1)] for _ in range(X+1)]
    dp[A][B][C] = 1
    for a in range(X+1):
        for b in range(X+1):
            for c in range(X+1):
                if a+b+c == 0:
                    continue
                dp[a][b][c] *= a+b+c
                if a > 0:
                    dp[a][b][c] += dp[a-1][b][c]*a
                if b > 0:
                    dp[a][b][c] += dp[a+1][b-1][c]*b
                if c > 0:
                    dp[a][b][c] += dp[a][b+1][c-1]*c
                dp[a][b][c] /= a+b+c
    ans = 0
    for a in range(X+1):
        for b in range(X+1):
            for c in range(X+1):
                if a+b+c == 0:
                    continue
                ans += dp[a][b][c]*abs(a-A)
                ans += dp[a][b][c]*abs(b-B)
                ans += dp[a][b][c]*abs(c-C)
    print(ans)

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    # A, B, C = 31, 41, 59
    # A, B, C = 0, 0, 1
    # A, B, C = 98, 99, 99
    # A, B, C = 99, 99, 99
    N = A + B + C
    prob = [A/N, B/N, C/N]
    dp = [[0]*(N+1) for _ in range(3)]
    for i in range(3):
        for j in range(N+1):
            if i == 0:
                if j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + dp[i][j-1]
            else:
                if j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = prob[i]*dp[i][j-1] + prob[i-1]*dp[i-1][j]
    print(dp[2][N])

=======
Suggestion 6

def main():
    A,B,C = map(int,input().split())
    p = [A/(A+B+C),B/(A+B+C),C/(A+B+C)]
    dp = [[0]*(101) for _ in range(101)]
    for i in range(1,101):
        for j in range(101):
            dp[i][j] = (i*p[0]+j*p[1]+(100-i-j)*p[2]+dp[i-1][j]+dp[i][j-1])/100
    print(dp[100][100])

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    print(A/(A+B+C)*B/(A+B+C-1)*C/(A+B+C-2) + B/(A+B+C)*A/(A+B+C-1)*C/(A+B+C-2) + C/(A+B+C)*A/(A+B+C-1)*B/(A+B+C-2) + 1)

=======
Suggestion 8

def main():
    a,b,c=map(int,input().split())
    s=a+b+c
    print(1+((a/s)*(1+((a-1)/(s-1))))+((b/s)*(1+((b-1)/(s-1))))+((c/s)*(1+((c-1)/(s-1)))))

=======
Suggestion 9

def main():
    #input
    A, B, C = map(int, input().split())
    #compute
    #output
    print(A*B*C/(A*B+A*C+B*C))
