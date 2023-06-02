Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    print(a+b+c+9)

=======
Suggestion 2

def main():
    a,b,c = map(int, input().split())
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

=======
Suggestion 3

def cal(a, b, c):
    return 10 * a + b + c

a, b, c = map(int, input().split())
print(max(cal(a, b, c), cal(b, a, c), cal(c, a, b), cal(a, c, b), cal(b, c, a), cal(c, b, a)))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A*10+B+C, A+B*10+C, A+B+C*10))

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    print(a+b+c+max(a,b,c)*9)

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    print(A+B+C+max(A, B, C)*9)

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B-C, A*B+C, A*B-C, A-B+C, A-B-C))

=======
Suggestion 8

def main():
    # 读取数据
    a,b,c = map(int,input().split())

    # 计算结果
    result = max(a+b+c,(a+b)*c,a*(b+c),a*b*c)

    # 输出结果
    print(result)
