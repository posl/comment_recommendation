Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    # 读入数据
    s1 = input()
    s2 = input()

    # 初始化
    flag = False

    # 处理
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        flag = True

    # 输出结果
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[0] == '.' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '#' and s2[1] == '.':
        print('No')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '.' and s2[1] == '#':
        print('No')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '#' and s2[1] == '.':
        print('No')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '.' and s2[1] == '#':
        print('No')
    elif s1[0] == '.' and s1[1] == '.' and s2[0] == '#' and s2[1] == '#':
        print('No')
    elif s1[0] == '.' and s1[1] == '.' and s2[0] == '#' and s2[1] == '.':
        print('No')
    elif s1[0] == '.' and s1[1] == '.' and s2[0] == '.' and s2[1] == '#':
        print('No')

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def solve():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[2] == '#' or s2[0] == '#' and s2[2] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    #输入
    S_1 = input()
    S_2 = input()
    #判断
    if (S_1[0] == "#" and S_1[1] == "#") or (S_1[0] == "#" and S_2[0] == "#") or (S_1[1] == "#" and S_2[1] == "#") or (S_2[0] == "#" and S_2[1] == "#"):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s_1 = input()
    s_2 = input()
    if s_1[0] == '#' and s_1[1] == '#' and s_2[0] == '#' and s_2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    if s1[0] == "#" and s1[2] == "#" and s2[0] == "#" and s2[2] == "#":
        print("Yes")
    else:
        print("No")
