Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(s[1:]+s[0])

=======
Suggestion 2

def move_str(str):
    return str[1:]+str[0]

=======
Suggestion 3

def move(s):
    return s[1:]+s[0]

=======
Suggestion 4

def main():
    S = input()
    print(S[1:] + S[0])

=======
Suggestion 5

def move_char(s):
    return s[1:]+s[0]

print(move_char(input()))

=======
Suggestion 6

def main():
    # 从标准输入中读取字符串
    s = input()
    # 将字符串的第一个字符移到末尾
    s = s[1:] + s[0]
    # 打印结果
    print(s)
