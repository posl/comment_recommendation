Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    s_index = 0
    t_index = 0
    while s_index < s_len and t_index < t_len:
        if s[s_index] == t[t_index]:
            s_index += 1
            t_index += 1
        else:
            t_index += 1
    if s_index == s_len:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            if s == t:
                print("Yes")
                return
    print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s == t[:-1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    slen = len(s)
    tlen = len(t)
    if slen > tlen:
        print("No")
        return
    for i in range(tlen-slen+1):
        if s == t[i:i+slen]:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    else:
        print("No")
        return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    else:
        print("No")
        return

=======
Suggestion 9

def solve():
    s = input()
    t = input()
    while True:
        if s == t:
            print("Yes")
            break
        if len(s) >= len(t):
            print("No")
            break
        if t[-1] == "A":
            t = t[:-1]
        else:
            t = t[:-1][::-1]
