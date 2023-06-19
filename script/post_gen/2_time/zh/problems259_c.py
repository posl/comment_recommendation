Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def solve():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    if len(s) == len(t):
        print('No')
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[:i] + s[i + 1:] == t[:i] + t[i + 1:]:
                print('Yes')
                return
            else:
                print('No')
                return
    print('No')

=======
Suggestion 3

def main():
    # 读取输入
    s = input()
    t = input()

    # 从s中删除t中不存在的字符
    for i in range(len(t)):
        if t[i] not in s:
            print('No')
            return
        else:
            s = s[s.index(t[i])+1:]

    print('Yes')
    return

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print("No")
        return
    i = 0
    j = 0
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i += 1
        else:
            if i == j:
                j += 1
            else:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) < 2 or len(s) > 2 * 10 ** 5 or len(t) < 2 or len(t) > 2 * 10 ** 5:
        return
    if s == t:
        print("Yes")
        return
    if s[0] != t[0]:
        print("No")
        return
    if s[-1] != t[-1]:
        print("No")
        return
    if s[1] == t[1]:
        print("Yes")
        return
    if s[-2] == t[-2]:
        print("Yes")
        return
    print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()

    if len(s) + 1 == len(t):
        if s == t[:-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 7

def solve():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s + s[0] == t:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 9

def solve(s,t):
    if len(s) > len(t):
        return False
    elif len(s) == len(t):
        return s == t
    else:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
