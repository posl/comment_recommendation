Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    x = int(input())
    # 检查是否满足条件
    if 0 <= x <= 1000 and x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    # 读取输入
    x = int(input())
    # 钱包里至少有一个100日元的硬币
    if x >= 100:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x = int(input())
    if x%100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    X = int(input())
    if X % 100 == 0 and X != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    # X = int(input())
    # if 0 <= X <= 1000:
    #     print("Yes")
    # else:
    #     print("No")
    print("Yes" if 0 <= int(input()) <= 1000 else "No")

=======
Suggestion 6

def main():
    x = int(input())
    if x % 100 == 0 and x >= 100 and x <= 1000:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def isPossible(x):
    for i in range(0, 15):
        for j in range(0, 15):
            if (i * 4 + j * 7) == x:
                return True
    return False
