Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    row = 2
    col = 2
    s1 = input()
    s2 = input()
    s1 = s1.replace('.', '')
    s2 = s2.replace('.', '')
    if len(s1) == 1 and len(s2) == 1:
        print("No")
    else:
        print("Yes")

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

def problem229_a():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def readinput():
    s1=input()
    s2=input()
    return s1,s2

=======
Suggestion 5

def solve():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')
    return 0

=======
Suggestion 6

def main():
    S_1 = input()
    S_2 = input()
    if S_1[0] == '#' and S_1[1] == '#' and S_2[0] == '#' and S_2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    # 读入数据
    s1 = input()
    s2 = input()
    # 计算黑色方格的个数
    cnt1 = s1.count('#')
    cnt2 = s2.count('#')
    # 判断是否可以从每个黑色方格到达每个黑色方格
    if cnt1 >= 2 and cnt2 >= 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()

    if s1[0] == '#' and s1[2] == '#' or s2[0] == '#' and s2[2] == '#' or s1[1] == '#' and s2[1] == '#' or s1[1] == '#' and s2[2] == '#' or s1[2] == '#' and s2[1] == '#':
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def problems229_a():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')
