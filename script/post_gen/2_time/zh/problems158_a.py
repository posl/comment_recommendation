Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入S
    S = input()
    # 初始化计数器
    count = 0
    # 循环统计S中B的个数
    for i in range(3):
        if S[i] == 'B':
            count += 1
    # 判断B的个数
    if count == 1 or count == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 2:
        print("Yes")
    elif s.count('B') == 1 and s.count('A') == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 2:
        print('Yes')
    elif s.count('A') == 2 and s.count('B') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    # 读取输入
    s = input()
    # 逻辑处理
    if s[0] == s[1] == s[2]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print("No")
    else:
        print("Yes")
