Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(s[1:] + s[0])

=======
Suggestion 2

def move(str):
    str = str[1:]+str[0]
    return str

=======
Suggestion 3

def main():
    # 读取输入
    S = input()
    # 处理
    S = S[1:] + S[0]
    # 输出
    print(S)

=======
Suggestion 4

def move(s):
    return s[1:]+s[0]

=======
Suggestion 5

def move(s):
    s = list(s)
    s.append(s[0])
    s.pop(0)
    s = "".join(s)
    return s

s = input()
print(move(s))
