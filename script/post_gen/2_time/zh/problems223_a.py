Synthesizing 10/10 solutions

=======
Suggestion 1

def is_100yen(x):
    if x % 100 == 0:
        return True
    else:
        return False

=======
Suggestion 2

def main():
    x = int(input())
    if x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    # 读取输入
    x = int(input())
    # 确定是否可以用x个100日元的硬币凑出x日元
    if x % 100 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def solve():
    X = int(input())
    if X % 100 == 0 and X != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def judge(x):
    if x % 100 == 0:
        return True
    else:
        return False

=======
Suggestion 7

def get_input():
    #get input
    x = int(input())
    return x

=======
Suggestion 8

def main():
    x = int(input())
    if x >= 100 and x % 100 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def question223_a():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def judge(X):
    if X>=100 and X%100==0:
        return True
    else:
        return False

X = int(input())
