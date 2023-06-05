Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s.count('o') == 1 or s.count('x') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s.find('o') != -1 and s.find('x') != -1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    print('Yes' if 'o' in s else 'No')

=======
Suggestion 4

def main():
    S = input()
    T = 'x' * 100000
    if S in T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    # 读取输入
    S = input()
    # 判断
    if "o" in S and "x" in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def sub_string(s):
    if s.count('o') == 0 or s.count('x') == 0:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 7

def main():
    # 读取数据
    str = input()
    # 处理数据
    if str.count('o') == 0 or str.count('x') == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    t = input()
    if t == 'o' or t == 'x':
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s = input()
    if s.count('o') == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    s = input()
    if s.find("o") > -1 and s.find("x") > -1:
        print("Yes")
    else:
        print("No")
