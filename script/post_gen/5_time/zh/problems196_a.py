Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a - c, a - d, b - c, b - d))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(b - c)

=======
Suggestion 3

def main():
    # 读取输入
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # 计算并输出答案
    print(max(a - c, a - d, b - c, b - d))

=======
Suggestion 4

def max_sub(a,b,c,d):
    return max(a*c,a*d,b*c,b*d)

=======
Suggestion 5

def f(a, b, c, d):
    return max(a * c, a * d, b * c, b * d)

a, b = map(int, input().split())
c, d = map(int, input().split())
print(f(a, b, c, d))
