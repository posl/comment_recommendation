Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    A, B, C = map(int, input().split())
    print((A+B+C) * (100 - A - B - C) / (A+B+C))

=======
Suggestion 2

def solve(a,b,c):
    table = [[[0 for i in range(100)] for j in range(100)] for k in range(100)]
    for i in range(99,-1,-1):
        for j in range(99,-1,-1):
            for k in range(99,-1,-1):
                if i+j+k == 0:
                    continue
                if i+j+k == 100:
                    continue
                table[i][j][k] = 1
                if i < 99:
                    table[i][j][k] += table[i+1][j][k] * i/(i+j+k)
                if j < 99:
                    table[i][j][k] += table[i][j+1][k] * j/(i+j+k)
                if k < 99:
                    table[i][j][k] += table[i][j][k+1] * k/(i+j+k)
    return table[a][b][c]

=======
Suggestion 3

def solve():
    A, B, C = map(int, input().split())
    dp = [[[0.0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    for a in range(100, -1, -1):
        for b in range(100, -1, -1):
            for c in range(100, -1, -1):
                if a == 100 or b == 100 or c == 100:
                    continue
                if a + b + c == 0:
                    continue
                dp[a][b][c] = (
                    (dp[a + 1][b][c] * a + dp[a][b + 1][c] * b + dp[a][b][c + 1] * c + 100) / (a + b + c)
                )
    return dp[A][B][C]

print(solve())

=======
Suggestion 4

def solve():
    A, B, C = map(int, input().split())
    dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    dp[A][B][C] = 0
    for a in range(A, 100):
        for b in range(B, 100):
            for c in range(C, 100):
                if a == 99 and b == 99 and c == 99:
                    continue
                dp[a+1][b][c] += dp[a][b][c] * a / (a+b+c)
                dp[a][b+1][c] += dp[a][b][c] * b / (a+b+c)
                dp[a][b][c+1] += dp[a][b][c] * c / (a+b+c)
                dp[a][b][c] += 1
    print(dp[99][99][99])

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    print((100-a)/a+(100-b)/b+(100-c)/c)

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        print(0)
        return
    if a == 0 or b == 0 or c == 0:
        print(100)
        return
    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    dp[a][b][c] = 1
    for i in range(a,100):
        for j in range(b,100):
            for k in range(c,100):
                if i == 0 and j == 0 and k == 0:
                    continue
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 100
                    continue
                dp[i][j][k] = (dp[i+1][j][k]*i + dp[i][j+1][k]*j + dp[i][j][k+1]*k) / (i+j+k) + 1
    print(dp[a][b][c])
    return

=======
Suggestion 7

def calc_expectation(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0

    if (a, b, c) in memo:
        return memo[(a, b, c)]

    ans = 0
    ans += calc_expectation(a+1, b, c) * a
    ans += calc_expectation(a, b+1, c) * b
    ans += calc_expectation(a, b, c+1) * c
    ans += 100
    ans /= (a+b+c)

    memo[(a, b, c)] = ans
    return ans

memo = {}
a, b, c = map(int, input().split())
print(calc_expectation(a, b, c))

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    print((a*b*c)/((a*b)+(b*c)+(c*a)))

=======
Suggestion 9

def solve(a,b,c):
    if a==100 or b==100 or c==100:
        return 0
    if a==0 and b==0 and c==0:
        return 0
    ans=0
    ans+=a/(a+b+c)*(1+solve(a+1,b-1,c))
    ans+=b/(a+b+c)*(1+solve(a,b+1,c-1))
    ans+=c/(a+b+c)*(1+solve(a-1,b,c+1))
    return ans

a,b,c=map(int,input().split())
print(solve(a,b,c))

=======
Suggestion 10

def main():
    a, b, c = map(int, input().split())
    print((a**2+b**2+c**2-a-b-c)/2/(a+b+c))
