Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input().strip().split()
    t = input().strip().split()
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    # 读入数据
    s = input()
    t = input()

    # 处理数据
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    s = input().split()
    t = input().split()
    for i in range(3):
        if s[i] == t[i]:
            continue
        else:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 5

def solve():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a = input()
    b = input()
    if a == b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    # 读入数据
    s = input()
    t = input()

    # 判断是否可以
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def swap_hat(hat1, hat2):
    return hat2, hat1
