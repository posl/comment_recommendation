Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print(1000 - N % 1000)

=======
Suggestion 2

def main():
    # 读取输入
    N = int(input())
    # 处理
    # 输出
    print(1000 - N % 1000 if N % 1000 != 0 else 0)

=======
Suggestion 3

def solve():
    # 请在这里编写代码
    n = int(input())
    print(1000 - n % 1000)

=======
Suggestion 4

def main():
    n = int(input())
    print(1000 - n % 1000)

=======
Suggestion 5

def main():
    n = int(input())
    print(1000-n%1000 if n%1000!=0 else 0)

=======
Suggestion 6

def problems173_a():
    N = int(input())
    print(1000 - N % 1000)

=======
Suggestion 7

def exchange(n):
    if n%1000 == 0:
        return 0
    else:
        return 1000 - n%1000

=======
Suggestion 8

def get_change(n):
    if n < 1000:
        return 1000 - n
    else:
        return n % 1000
