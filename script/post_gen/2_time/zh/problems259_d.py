Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    while len(s) < len(t):
        if s[-1] == t[len(s)-1]:
            s = s + s[-1]
        else:
            break
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def diff(a,b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

s = input()
t = input()

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) < 2 or len(s) > 2*10**5 or len(t) < 2 or len(t) > 2*10**5:
        return
    if s == t:
        print("Yes")
        return
    i = 0
    while i < len(s):
        if i == len(s)-1:
            print("No")
            return
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            i += 2
        else:
            i += 1
    if s == t:
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 4

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len >= t_len:
        print("No")
        return
    else:
        t_index = 0
        for s_index in range(s_len):
            if s[s_index] == t[t_index]:
                t_index += 1
            else:
                if s_index == 0:
                    print("No")
                    return
        print("Yes")
        return

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            else:
                if s[i] == t[i+1]:
                    continue
                else:
                    print("No")
                    exit()
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
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
Suggestion 7

def main():
    # s = input()
    # t = input()
    s = 'abbaac'
    t = 'abbbbaaac'
    if len(s) < 2 or len(s) > 2*10**5 or len(t) < 2 or len(t) > 2*10**5:
        print('No')
        return
    if s == t:
        print('Yes')
        return
    if s[0] != t[0]:
        print('No')
        return
    if s[-1] != t[-1]:
        print('No')
        return
    if s[-2] != t[-2]:
        print('No')
        return
    if s[-3] != t[-3]:
        print('No')
        return
    print('Yes')

=======
Suggestion 8

def solve():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len >= t_len:
        print('No')
        return
    if s == t[:s_len]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        print('No')
