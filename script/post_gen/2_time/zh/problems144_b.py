Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a >= 1 and a <= 20 and b >= 1 and b <= 20:
        print(a*b)
    else:
        print(-1)

=======
Suggestion 2

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a < 1 or a > 20 or b < 1 or b > 20:
        print("输入的所有数值都是整数，而且1 ≦ A ≦ 20, 1 ≦ B ≦ 20")
        return
    print(a * b)

=======
Suggestion 4

def main():
    # 读取输入
    A, B = map(int, input().split())

    # 判断A, B是否在1到20之间
    if 1 <= A <= 20 and 1 <= B <= 20:
        # 计算A*B
        print(A * B)
    else:
        print(-1)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a * b)

=======
Suggestion 6

def main():
    import sys
    a, b = map(int, sys.stdin.readline().split())
    if a >= 1 and a <= 20 and b >= 1 and b <= 20:
        print(a * b)
    else:
        print(-1)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if 1 <= A <= 20 and 1 <= B <= 20:
        print(A * B)
    else:
        print(-1)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if 1 <= a <= 20 and 1 <= b <= 20:
        print(a * b)
    else:
        print(-1)
