Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[2] == '#' and s2[0] == '#' and s2[2] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def check(s):
    if s[0][0] == '#' and s[0][1] == '#' and s[1][0] == '#' and s[1][1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    # 读入数据
    S_1 = input()
    S_2 = input()
    # 处理数据
    if S_1[0] == '#' and S_1[1] == '#' and S_2[0] == '#' and S_2[1] == '#':
        print('Yes')
    else:
        print('No')
    # 输出结果

=======
Suggestion 6

def get_input():
    s1 = input()
    s2 = input()
    return s1, s2

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    if(s1[0] == "#" and s1[1] == "#" and s2[0] == "#" and s2[1] == "#"):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')
