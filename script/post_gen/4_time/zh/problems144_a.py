Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a > 9 or b > 9:
        print("-1")
    else:
        print(a*b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a * b)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a > 0 and a < 10 and b > 0 and b < 10:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 4

def problems144_a():
    a,b = map(int,input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

=======
Suggestion 5

def main():
    # 读取输入
    A, B = map(int, input().split())

    # 计算
    if (A >= 1 and A <= 20) and (B >= 1 and B <= 20):
        print(A * B)
    else:
        print(-1)

=======
Suggestion 6

def main():
    a,b=map(int,input().split())
    if a>=1 and a<=20 and b>=1 and b<=20:
        print(a*b)
    else:
        print(-1)
main()

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a >= 1 and a <= 20 and b >= 1 and b <= 20:
        print(a*b)
    else:
        print(-1)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a <= 20 and b <= 20:
        print(a * b)
    else:
        print(-1)
