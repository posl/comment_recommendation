Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(a * b - (a + b - 1))

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    print(a*b-1)

=======
Suggestion 3

def main():
    # 读取输入
    a,b = map(int, input().split())
    # 计算并输出
    print(a*b-1)

=======
Suggestion 4

def main():
    # 读取数据
    with open('problems106_a.txt') as f:
        A, B = [int(i) for i in f.readline().split()]

    # 计算面积
    area = A * B - (A - 1) - (B - 1)

    # 输出结果
    print(area)

=======
Suggestion 5

def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算并输出结果
    print(a * b - 1)

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    print(A*B-1)

=======
Suggestion 7

def main():
    n = input().split()
    a = int(n[0])
    b = int(n[1])
    print(a*b-1)
