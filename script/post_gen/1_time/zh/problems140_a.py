Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print(N**3)

=======
Suggestion 2

def main():
    #N = 2
    N = int(input())
    print(N**3)

=======
Suggestion 3

def main():
    n = int(raw_input())
    print n**3

=======
Suggestion 4

def main():
    n = int(input())
    print(n**3)

=======
Suggestion 5

def main():
    # 1. 读入数据
    n = int(input())
    # 2. 处理数据
    # 3. 写出结果
    print(n**3)

=======
Suggestion 6

def count_passwords(n):
    if n == 1:
        return 1
    else:
        return count_passwords(n-1) * n
