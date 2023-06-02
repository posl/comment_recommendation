Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c = c-b
        if c <= 0:
            print("Yes")
            break
        a = a-d
        if a <= 0:
            print("No")
            break

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
        if a <= 0:
            print('No')
            break

=======
Suggestion 3

def main():
    # 读取输入
    line = input()
    # 用空格分割输入
    a, b, c, d = line.split()
    # 将输入转换为整数
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    # 用循环模拟游戏
    while True:
        # 高桥的回合
        c = c - b
        # 如果青木输了，就打印是
        if c <= 0:
            print("是")
            break
        # 青木的回合
        a = a - d
        # 如果高桥输了，就打印否
        if a <= 0:
            print("否")
            break

=======
Suggestion 4

def main():
    a, b, c, d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break

=======
Suggestion 5

def main():
    a, b, c, d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break

=======
Suggestion 6

def main():
    a,b,c,d = map(int,input().split())
    while a>0 and c>0:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
        if a <= 0:
            print('No')
            break

=======
Suggestion 7

def battle(a, b, c, d):
    while True:
        if c <= 0:
            return True
        elif a <= 0:
            return False
        c -= b
        a -= d
