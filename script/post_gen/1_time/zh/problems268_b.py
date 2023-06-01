Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S in T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T[0:len(S)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def is_prefix(s,t):
    if len(s) > len(t):
        return False
    if s == t[:len(s)]:
        return True
    else:
        return False

=======
Suggestion 7

def main():
    # 读取输入
    s = input()
    t = input()
    # 检查
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t[:len(s)]:
        print("Yes")
    else:
        print("No")
