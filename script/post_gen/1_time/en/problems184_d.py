Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print((a*(a+1) / (a+b+c)) + (b*(b+1) / (a+b+c)) + (c*(c+1) / (a+b+c)))

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    print((A * (A + 1) / (2 * A + B + C)) + (B * (B + 1) / (2 * B + C)) + (C * (C + 1) / (2 * C)))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print((a * (a + 1) * (a + 2) / (a + b + c) / (a + b + c + 1) + b * (b + 1) * (b + 2) / (a + b + c) / (a + b + c + 1) + c * (c + 1) * (c + 2) / (a + b + c) / (a + b + c + 1)) * 100)

=======
Suggestion 4

def solve():
    a,b,c = map(int, input().split())
    dp = [[[0.0]*(101) for _ in range(101)] for _ in range(101)]
    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            for k in range(99, -1, -1):
                if i+j+k == 0:
                    continue
                dp[i][j][k] = (dp[i+1][j][k]+1)*i/(i+j+k) + (dp[i][j+1][k]+1)*j/(i+j+k) + (dp[i][j][k+1]+1)*k/(i+j+k)
    print(dp[a][b][c])

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print((a*b*c)/((a+b)*(b+c)*(c+a)-a*b*c))

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    print((a*(100-a)/a) + (b*(100-b)/b) + (c*(100-c)/c))

=======
Suggestion 7

def solve():
    a,b,c = map(int,input().split())
    ans = 0
    while a+b+c >= 3:
        ans += 1
        if a == 0:
            b -= 1
            c -= 1
            a += 1
        elif b == 0:
            a -= 1
            c -= 1
            b += 1
        elif c == 0:
            a -= 1
            b -= 1
            c += 1
        else:
            a -= 1
            b -= 1
            c -= 1
            a += 1
    print(ans)

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    print((a*b*b*100 + a*c*c*100 + b*c*c*100)/(a*b*c*100 - a*b*b*100 - a*c*c*100 - b*c*c*100))

main()

=======
Suggestion 9

def solve(A: int, B: int, C: int)-> float:
    # write your code here
    return 0.0

=======
Suggestion 10

def solve():
    A,B,C = map(int,input().split())
    print((A*(A+1)/2)/(A+B+C))
