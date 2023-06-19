Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(s):
    for i in range(10):
        if str(i) not in s:
            return i

=======
Suggestion 2

def main():
    s = input()
    s = list(s)
    s = [int(i) for i in s]
    for i in range(1,10):
        if i not in s:
            print(i)
            break

=======
Suggestion 3

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 4

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            return

=======
Suggestion 5

def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            break

=======
Suggestion 6

def find_missing_number(s):
    s = list(s)
    s = map(int, s)
    s.sort()
    for i in range(0, len(s)):
        if s[i] != i:
            return i
    return 9

=======
Suggestion 7

def main():
    # 从标准输入读取字符串
    s = input()
    # 从0到9的所有数字正好出现一次，那么0到9的和减去字符串s的和，就是缺少的数字
    print(45 - sum(map(int, s)))

=======
Suggestion 8

def get_missing_number(s):
    for i in range(10):
        if str(i) not in s:
            return i
