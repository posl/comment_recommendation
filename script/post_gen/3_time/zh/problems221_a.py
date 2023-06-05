Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B = map(int,input().split())
    print(32**(A-B))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(32 ** (a - b))

=======
Suggestion 3

def cal_energy(A, B):
    return 32 ** (A-B)

A, B = map(int, input().split())
print(cal_energy(A, B))

=======
Suggestion 4

def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算输出
    print(32 ** (A - B))
