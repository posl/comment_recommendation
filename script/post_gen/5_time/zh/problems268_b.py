Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T[:len(S)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t[:len(s)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def func(s,t):
    if t.startswith(s):
        return 'Yes'
    else:
        return 'No'

s = input()
t = input()
print(func(s,t))

=======
Suggestion 4

def main():
    # 读入S和T
    S = input()
    T = input()
    # 请在此添加您的代码
    if S == T[0:len(S)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if t[0:len(s)] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print('Yes')
    else:
        print('No')
