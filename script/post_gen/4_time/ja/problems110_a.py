Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(10 * a + b + c, a + 10 * b + c, a + b + 10 * c))

=======
Suggestion 2

def main():
    # input
    A, B, C = map(int, input().split())

    # compute

    # output
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(A+B+C+max(A, B, C)*9)

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(a+b+c+max(a, b, c)*9)

=======
Suggestion 6

def main():
    # input
    a, b, c = map(int, input().split())

    # compute

    # output
    print(max(a + b + c, a + b - c, a - b + c, -a + b + c))

=======
Suggestion 7

def main():
    A,B,C = map(int,input().split())
    print(max(10*A+B+C,10*B+A+C,10*C+A+B))

=======
Suggestion 8

def main():
    # 標準入力受け取り
    a, b, c = map(int, input().split())

    # 出力
    print(max(a + b + c, a + b * c, a * b + c, a * b * c))

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    print(10*a+b+c)
