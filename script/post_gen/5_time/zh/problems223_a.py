Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def judge(x):
    if x >= 100 and x % 100 == 0:
        return True
    else:
        return False

=======
Suggestion 2

def main():
    x = int(input())
    if x % 100 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    # 读入数据
    x = int(input())
    # 判断是否满足条件
    if x >= 100 and x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x = int(input())
    print('Yes' if x%100 == 0 and x != 0 else 'No')
    return 0

=======
Suggestion 5

def solution(X):
    if X % 100 == 0 and X != 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    X = int(input())
    if X % 100 == 0 and X // 100 > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    money = int(input())
    if money % 100 == 0:
        print('Yes')
    else:
        print('No')
