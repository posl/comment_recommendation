Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(m, h):
    if h % m == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    M, H = map(int, input().split())
    if H % M == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    m, h = map(int, input().split())
    if h % m == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    M, H = map(int, input().split())
    if H % M == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def f(m, h):
    if h % m == 0:
        print("Yes")
    else:
        print("No")

f(10, 120)
f(10, 125)

=======
Suggestion 6

def main():
    # 读入数据
    line = input()
    line = line.split()
    m = int(line[0])
    h = int(line[1])
    # 计算
    if h % m == 0:
        print("Yes")
    else:
        print("No")
