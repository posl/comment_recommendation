Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int, input().split())
    print(c - (a - b) if c >= (a - b) else c)

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a >= b + c:
        print(0)
    else:
        print(c - (a - b))

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(c if a >= b+c else a+b-c)

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if b >= a:
        print(c)
    else:
        print(c - (a - b))

=======
Suggestion 6

def main():
    # 读取输入
    A, B, C = map(int, input().split())

    # 从2号瓶中转移水
    C -= A - B

    # 答案
    print(C if C >= 0 else 0)

=======
Suggestion 7

def main():
    A,B,C = map(int,input().split())
    print(C if A >= B+C else A+B)
