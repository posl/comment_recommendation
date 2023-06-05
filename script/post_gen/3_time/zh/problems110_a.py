Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 计算结果
    print(max(a+b+c, a+b*c, a*b+c, a*b*c))

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    print(a+b+c*10)

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    print(a+b+c+max(a,b,c)*9)

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    print(max(a+b+c,a*10+b+c,a+b*10+c,a+b+c*10))

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    print(max(a+b+c,a+b*c,a*b+c,a*b*c))

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B-C, A-B+C, A-B-C, A+B*C, A+B*C, A-B*C, A-B*C))
