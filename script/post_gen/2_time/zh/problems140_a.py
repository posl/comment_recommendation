Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_passwords(n):
    if n == 1:
        return 1
    elif n == 2:
        return 8
    else:
        return 9 * 8 ** (n - 1)

=======
Suggestion 2

def main():
    N = int(input())
    print(pow(N, 3))

=======
Suggestion 3

def main():
    n = int(input())
    print(n**3)

=======
Suggestion 4

def main():
    n = int(raw_input())
    print n**3

=======
Suggestion 5

def main():
    # 读取输入
    n = int(input())
    # 计算答案
    ans = n**3
    # 输出答案
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    print(N**3)

=======
Suggestion 7

def get_passwords(n):
    if n == 1:
        return 1
    return n * n * n
