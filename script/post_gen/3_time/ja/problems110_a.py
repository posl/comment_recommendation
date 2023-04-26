Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(a + b + c + max(a, b, c) * 9)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    print(max(10*A+B+C, A+10*B+C, A+B+10*C))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(A+B+C+max(A*10+B+C, B*10+A+C, C*10+A+B))

=======
Suggestion 5

def main():
    # データ入力
    a, b, c = map(int, input().split())

    # 計算
    ans = a + b + c
    ans = max(ans, a + b * c)
    ans = max(ans, a * b + c)
    ans = max(ans, a * b * c)
    ans = max(ans, a * (b + c))
    ans = max(ans, (a + b) * c)

    # 結果出力
    print(ans)

=======
Suggestion 6

def main():
    a, b, c = list(map(int, input().split()))
    print(10 * max(a, b, c) + a + b + c)

=======
Suggestion 7

def main():
    # 整数の入力
    a, b, c = map(int, input().split())
    print(a+b+c+max(a,b,c)*9)

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())

    print(10 * a + b + c)
