Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    C = input()
    if C[0] == C[1] == C[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 2

def f(c1,c2,c3):
    if c1==c2 and c1==c3 and c2==c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 3

def main():
    # 读入
    input = raw_input()
    # 分割
    input_list = input.split()
    # 判断
    if input_list[0] == input_list[1] == input_list[2]:
        print "Won"
    else:
        print "Lost"

=======
Suggestion 4

def main():
    c1, c2, c3 = input().split()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 5

def main():
    # 读取输入
    s = input()
    # 输出结果
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 6

def main():
    # 从标准输入读取
    str = input()
    # 判断是否是赢了
    if str[0] == str[1] and str[1] == str[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 7

def main():
    c = input()
    if c[0] == c[1] and c[1] == c[2]:
        print("Won")
    else:
        print("Lost")
main()

=======
Suggestion 8

def main():
    str = input()
    if str.count(str[0]) == 3:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 9

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print("Won")
    else:
        print("Lost")
