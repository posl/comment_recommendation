Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    c1, c2, c3 = input().split()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 2

def main():
    c1, c2, c3 = input().split()
    if c1 == c2 == c3:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 3

def main():
    # 输入
    C = input()
    # 处理
    if C[0] == C[1] == C[2]:
        result = "Won"
    else:
        result = "Lost"
    # 输出
    print(result)

=======
Suggestion 4

def main():
    print("请输入三个大写的英文字母，以空格隔开：")
    str = input()
    strList = str.split(" ")
    if strList[0] == strList[1] == strList[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 5

def problem189_a():
    #读取输入
    C = input()
    #判断是否胜利
    if C[0] == C[1] == C[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 6

def problem189_a():
    c1,c2,c3 = input().split()
    if c1 == c2 and c2 == c3:
        print("Won")
    else:
        print("Lost")

problem189_a()

=======
Suggestion 7

def main():
    result = input()
    if result[0] == result[1] == result[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 8

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 9

def main():
    # 读取输入
    s = input()
    # 判断是否胜利
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 10

def main():
    c1,c2,c3 = input().split()
    if c1 == c2 and c2 == c3:
        print("Won")
    else:
        print("Lost")
