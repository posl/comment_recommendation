Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int, input().split())
    print((a*b*c)/(a*b+b*c+c*a))

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    print(100*(a/(a+b+c)))

=======
Suggestion 3

def main():
    A,B,C = map(int,input().split())
    print(100-C)

=======
Suggestion 4

def main():
    print('Hello World!')

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print((a * (a + b + c - 1) + b * (b + c - 1) + c * (c - 1)) / (a + b + c - 1))

=======
Suggestion 6

def main():
    A,B,C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    n = 0
    while A != 100 and B != 100 and C != 100:
        n += 1
        if A == 0:
            A += 1
            B -= 1
            C -= 1
        elif B == 0:
            B += 1
            A -= 1
            C -= 1
        elif C == 0:
            C += 1
            A -= 1
            B -= 1
        else:
            i = random.randint(1,3)
            if i == 1:
                A += 1
                B -= 1
                C -= 1
            elif i == 2:
                B += 1
                A -= 1
                C -= 1
            else:
                C += 1
                A -= 1
                B -= 1
    print(n)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def solve():
    a,b,c = map(int,input().split())
    print(100/(1-(a+b+c)/100))

=======
Suggestion 9

def solve():
    # 读入数据
    a, b, c = map(int, input().split())

    # 用动态规划求解
    # dp[i][j][k]: 从(i, j, k)状态开始，直到100个相同颜色的硬币出现的期望操作次数
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]
    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            for k in range(99, -1, -1):
                if i == 99 and j == 99 and k == 99:
                    continue
                if i + j + k == 0:
                    continue
                # 求解dp[i][j][k]
                dp[i][j][k] = (i * dp[i + 1][j][k] + j * dp[i][j + 1][k] + k * dp[i][j][k + 1]) / (i + j + k) + 1

    # 输出结果
    print(dp[a][b][c])
