Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    A,B = map(int,input().split())
    print(max(0,A-2*B))

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    print(max(a-2*b,0))

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A <= B:
        print(0)
    else:
        print(A-B*2)

=======
Suggestion 4

def main():
    a,b = map(int, raw_input().split())
    print max(0, a-2*b)

=======
Suggestion 5

def get_input():
    #获取输入
    input_str = input()
    input_list = input_str.split()
    return input_list

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    print(max(0,a-b*2))

=======
Suggestion 7

def problems143_a():
    a,b = map(int,input().split())
    if a >= b:
        print(a-b)
    else:
        print(0)

problems143_a()

=======
Suggestion 8

def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算并输出结果
    print(max(0, A - B * 2))

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    if A < B:
        print(0)
    else:
        print(A-2*B)

=======
Suggestion 10

def main():
    a,b = map(int,input().split())
    if a > b:
        print(a-b)
    else:
        print(0)
